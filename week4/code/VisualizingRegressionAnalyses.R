# Visualizing Regression analyses — subset by Predator.lifestage
# 输出：results/regressions_by_lifestage.csv  和  results/predator_prey_regressions.pdf

# —— 依赖包 —— #
pkgs <- c("tidyverse","broom")
invisible(lapply(pkgs, function(p) if (!requireNamespace(p, quietly = TRUE)) install.packages(p)))
library(tidyverse)
library(broom)

# —— I/O 路径（可按需修改）—— #
infile  <- "../data/EcolArchives-E089-51-D1.csv"
outdir  <- "results"
outfile_csv <- file.path(outdir, "regressions_by_lifestage.csv")
outfile_pdf <- file.path(outdir, "predator_prey_regressions.pdf")

if (!dir.exists(outdir)) dir.create(outdir, recursive = TRUE)

# —— 读数与清洗 —— #
df <- read.csv(infile, stringsAsFactors = FALSE)

# 只保留分析所需变量，并统一类型
df <- df %>%
  transmute(
    Predator.lifestage = as.factor(Predator.lifestage),
    Predator.mass      = as.numeric(Predator.mass),
    Prey.mass          = as.numeric(Prey.mass),
    Prey.mass.unit     = Prey.mass.unit
  )

# 单位统一：mg → g
df$Prey.mass[df$Prey.mass.unit == "mg"] <- df$Prey.mass[df$Prey.mass.unit == "mg"] / 1000
df$Prey.mass.unit <- "g"

# 过滤缺失与非正数（log10 需要）
dat <- df %>%
  filter(is.finite(Predator.mass), is.finite(Prey.mass),
         Predator.mass > 0, Prey.mass > 0,
         !is.na(Predator.lifestage))

# 添加对数列
dat <- dat %>%
  mutate(
    log10Pred = log10(Predator.mass),
    log10Prey = log10(Prey.mass)
  )

# —— 按生命阶段分组回归：log10(Prey) ~ log10(Predator) —— #
models <- dat %>%
  group_by(Predator.lifestage) %>%
  group_map(~ lm(log10Prey ~ log10Pred, data = .x), .keep = TRUE)

names(models) <- levels(dat$Predator.lifestage)

# 整理系数表 & 模型摘要
coef_tbl <- map2_dfr(
  models, names(models),
  ~ tidy(.x) %>%
    mutate(Predator.lifestage = .y) %>%
    select(Predator.lifestage, term, estimate, std.error, statistic, p.value)
)

glance_tbl <- map2_dfr(
  models, names(models),
  ~ glance(.x) %>%
    mutate(Predator.lifestage = .y) %>%
    select(Predator.lifestage, r.squared, adj.r.squared, sigma, AIC, BIC, df = df.residual, p.value)
)

n_tbl <- dat %>%
  count(Predator.lifestage, name = "n")

# 合并成一个清晰结果表：每组给出截距与斜率行各一条，也可透视成宽表
res_long <- coef_tbl %>%
  left_join(glance_tbl, by = "Predator.lifestage") %>%
  left_join(n_tbl, by = "Predator.lifestage") %>%
  arrange(Predator.lifestage, match(term, c("(Intercept)", "log10Pred")))

# 也提供一个“宽表”（每组一行：斜率、截距、R2、N等）
res_wide <- res_long %>%
  select(Predator.lifestage, term, estimate, std.error, statistic, p.value,
         r.squared, adj.r.squared, sigma, AIC, BIC, df, n) %>%
  pivot_wider(
    names_from = term,
    values_from = c(estimate, std.error, statistic, p.value),
    names_glue = "{term}.{.value}"
  ) %>%
  # 便于阅读重命名
  rename(
    intercept      = `(Intercept).estimate`,
    slope          = `log10Pred.estimate`,
    intercept_se   = `(Intercept).std.error`,
    slope_se       = `log10Pred.std.error`,
    intercept_t    = `(Intercept).statistic`,
    slope_t        = `log10Pred.statistic`,
    intercept_p    = `(Intercept).p.value`,
    slope_p        = `log10Pred.p.value`
  ) %>%
  arrange(Predator.lifestage)

# 写出 CSV（含宽表，附在下方；若你只想要 res_long，把对象换掉即可）
write.csv(res_wide, outfile_csv, row.names = FALSE)

# —— 画图：按生命阶段分面，散点 + 回归线 —— #
p <- ggplot(dat, aes(x = log10Pred, y = log10Prey)) +
  geom_point(alpha = 0.35, size = 1) +
  geom_smooth(method = "lm", se = FALSE, linewidth = 0.8) +
  facet_wrap(~ Predator.lifestage, scales = "free") +
  labs(
    x = expression(log[10]*"(Predator mass, g)"),
    y = expression(log[10]*"(Prey mass, g)"),
    title = "Predator–Prey body mass regressions by predator lifestage"
  ) +
  theme_bw(base_size = 12) +
  theme(panel.grid = element_blank())

ggsave(outfile_pdf, p, width = 9, height = 6, units = "in", dpi = 300)

message("Done.\nCSV: ", outfile_csv, "\nPDF: ", outfile_pdf)


