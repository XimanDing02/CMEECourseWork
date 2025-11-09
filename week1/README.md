# Week 1 – UNIX, Shell scripting, Git and LaTeX

## Table of Contents
- [**Week 1** – Introduction to UNIX, Shell scripting, and LaTeX](#week-1--introduction-to-unix-shell-scripting-and-latex)
  - [**Project Structure**](#project-structure)
  - [**Brief Description**](#brief-description)
  - [**Dependencies**](#dependencies)
  - [**Languages**](#languages)
  - [**Installation**](#installation)
  - [**UNIX and Linux**](#unix-and-linux)
  - [**Shell scripting**](#shell-scripting)
  - [**Git**](#git)
  - [**LaTeX**](#latex)# Week 1 – UNIX, Shell scripting, Git and LaTeX

## Project Structure
This whole week1 structure is:
```plaintext
./week1/
│
├── code/
│   ├── UnixPrac1.txt
│   ├── boilerplate.sh
│   ├── variables.sh
│   ├── MyExampleScript.sh
│   ├── CountLines.sh
│   ├── tabtocsv.sh
│   ├── csvtospace.sh
│   ├── ConcatenateTwoFiles.sh
│   ├── tiff2png.sh
│   ├── FirstExample.tex
│   ├── FirstBiblio.bib
│   └── CompileLaTeX.sh
│
├── data/
│   ├── fasta/
│   │   ├── 407228326.fasta
│   │   ├── 407228412.fasta
│   │   └── E.coli.fasta
│   ├── Temperatures/
│   │   ├── sample1.csv
│   │   ├── sample2.csv
│   │   └── sample1.space
│   └── spawannxs.txt
│
├── results/
│   └── (currently empty — will store output from scripts)
│
└── sandbox/
    └── (temporary files for command testing, excluded via .gitignore)
```

## Brief Description

This week introduces foundational computing tools:

1. Unix and Linux command
2. Basic shell scripting and file manipulation
3. Version control with Git
4. LaTex to do some of the scientific writing
5. These works are based on the Notebook and Data from https://github.com/mhasoba/TheMulQuaBio.git.

## Languages
```
Bash, Unix Shell, Shell script, Git, LaTeX
```

## **Installation**
```
Ensure that you are using a UNIX-based environment.

git clone https://github.com/XimanDing02/CMEECourseWork.git
```

## **Dependencies** 

Most of the scripts in the current repository can be ran in bash shell directly. One of the scripts `tiff2png.sh` needs the imagemagick. 

Installation: `sudo apt install imagemagick` (Run in the terminal)

##  UNIX and Linux
This is the first part of this week. In this section, we learned to write commands within UNIX/Linux,  and practiced a range of basic terminal commands to make myself be more and more familiar with the terminal (because terminal is quite a new thing to me). The goal for this week was to understand directory structures, file management, command and how to combine commands efficiently using pipes and redirection.

### What I did
We started by understanding the UNIX system and building my CMEECoureseWork/week1 directory with sub-directories (code, data, result and sandbox). Then we learned how to navigate through the file system, use Linux command to create, move and manage files. We also practiced combining commands with pipes and redirection to handle tasks more efficiently.

### UnixPrac1.txt - FASTA exercise
I used such as `wc`, `tail`, `tr`, `grep`, and `awk` to write five commands, and combined them into **`UnixPrac1.txt`**, located in the `week1/code/` directory:

1. **Count the number of lines in each file** 

`wc -l ../data/fasta/*.fasta`

`wc` =  word count; `-l` indicates that we only count lines; `.../data/fasta/*` is to path all the docyments inside the fasta filedirectory. 

2. **Print everything starting from the second line for the E. coli genome** 

`tail -n +2 ../data/fasta/E.coli.fasta`

`tail` means we want to print the last part of the document; `-n +2` means we want to start displaying from line 2 onward; `.../data/fasta/E_coli.fasta` is the path to the target file.

3. **Count the sequence length of this genome** 

`tail -n +2 ../data/fasta/E.coli.fasta | tr -d '\n' | wc -m`

`tail -n +2` is same as that in Q2, which means that we want to count from line 2 to the end; `.../data/fasta/E_coli.fasta` is the path to target file; `|` ends that output to `tr -d '\n'` which removes all newline characters; `wc -m` counts all characters.

4. **Count the matches of a particular sequence, “ATGC” in the genome of E. coli** 

`tail -n +2 ../data/fasta/E.coli.fasta | tr -d '\n' | grep -o "ATGC" | wc -l`

All the first part are the same as above. `tr -d '\n'` removes all newlines. `grep -o` "ATGC" searches for every exact match of "ATGC" and prints each match on a new line; `wc -l` only counts lines.

5. **Compute the (A+T)/(G+C) ratio** 

```
tail -n +2 ../data/fasta/E.coli.fasta | tr -d '\n' | \
awk '{seq=$0; A=gsub(/A/, "", seq); T=gsub(/T/, "", seq); G=gsub(/G/, "", seq); C=gsub(/C/, "", seq); print (A+T)/(G+C)}'
```

All the first part are the same as above. `tr -d '\n'` removes all newlines. awk command: `.gsub(/A/,"")` counts how many A bases appear, other letters are same way. print (A+T)/(G+C) calculates the ratio of (A+T) to (G+C) bases.

### Usage
Example commands:
```
# You are now in CMEECourseWork
cd ~/CMEECourseWork/week1/code
bash UniPrac1.txt
```

## Shell scripting
In this section, we learned how to write and run bash shell scripts to automate repetitive tasks. We learned the structure and syntax of a shell script ad create seveal shell scripts which were saved in the `code/` directory.

### What I did
I wrote several shell scripts following the instructions in the book. And I would like to introduces them with their functions:

1. **boilerplate.sh** 

This ia a simple starting template for shell script template with author information, date (I put my information into this shell script), and a short description. When bash it, it shows: This is a shell script! 

```
# Basic Usage
# Example Command
bash boilerplate.sh
```

2. **variables.sh**

This is a shell script shows the use of special variables in bash(such as $0, $1, $#, $@) and user-defined variables (like MY_VAR='some string'). We can input some numbers and carry out some simple mathematical operations.

```
# Basic Usage
bash variables.sh [args]
# Example Command
bash variables.sh one two
```

3. **tabtocsv.sh**

Turns a tab-delimited text file into a comma-separated `.csv` file using the `tr` command. The new file is saved in the same folder with `.csv` added to the name. 

```
# Basic Usage
bash tabtocsv.sh <tab_file>
# Example Command
bash tabtocsv.sh ../sandbox/test.txt
```

4. **csvtospace.sh**

Replace commas with spaces in the `.csv` file. It checks for errors (such as missing inputs) and saves the new output file without overwriting the original file.

```
# Basic Usage
bash csvtospace.sh <csv_file>
# Example Command
bash csvtospace.sh ../data/Temperatures/temperatures.csv
```

5. **CountLines.sh**

`wl -l` count only lines of the targeted file. And, outputs the filenames and line count to the terminal.

```
# Basic Usage
bash CountLines.sh <filename>
# Example Command
bash CountLines.sh ../data/test.txt
```

6. **ConcatenateTwoFiles.sh**

ombines the contents of two files into a third one using `cat`. 

```
# Basic Usage
bash ConcatenateTwoFiles.sh <file1> <file2> <output>
# Example Command
bash ConcatenateTwoFiles.sh file1.txt file2.txt merged.txt
```

7. **tiff2png.sh**

Converts all `.tif` image files in the current folder into `.png` format using ImageMagick’s `convert` command. Uses a simple `for` loop. 

```
# Basic Usage
bash tiff2png.sh
# Example Command
bash tiff2png.sh
```

8. **MyExampleScript.sh**

This shell script demonstrates environment variables ($USER) and simple message printing.

```
# Basic Usage
bash MyExampleScript.sh
# Example Command
bash MyExampleScript.sh
```

## Git
This section introduced **Git** as a version control for tracking changes of the code and files, then managing collaborative work. 

### What we did
First, we learnt how to install Git though the terminal for version control, and then setting up our username and university email address. Then, I initialised a local repository. After that, I created an SSH connection though terminal linking the local repository to GitHub. Next, I practised creating and merging branches to safely test new code, configured the `.gitignore` file to exclude non-essential files such as logs and backups, and wrote a README.md file describing the first week's content.

## LaTeX
In this section, we were introduced to LaTex, but I used LaTex a lot when I was in my undergraduate degree. So this section is quite simple for me.

### What we did
I installed LaTex though terminal. Then I created the document **FirstExample.tex** with a title, abstract, sections, equations and references. Added a bibliography file **FirstBiblio,bib**. Then compiled the document and produced a fully LaTex **.pdf** document.

1. **FirstBiblio.bib**

BibTeX bibliography file containing references cited in FirstExample.tex.

```
# Basic Usage
Used automatically by LaTeX when compiling
```

2. **FirstExample.tex**

A minimal LaTeX document demonstrating use of titles, citations, and bibliography inclusion.

```
# Basic Usage
Compile using the script above
# Example Command
bash CompileLaTeX.sh ../data/FirstExample.tex
```

3. **CompileLaTeX.sh**

Compiles a LaTeX .tex file to .pdf, runs BibTeX if required, and cleans up auxiliary files.

```
# Basic Command
bash CompileLaTeX.sh <filename.tex>
# Example Command
bash CompileLaTeX.sh ../data/FirstExample.tex
```

## Author and Contact
Name: Ximan Ding
Email: x.ding25@imperial.ac.uk
Institution: Imperial College London