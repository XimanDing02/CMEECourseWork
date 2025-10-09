# Week 1 – Introduction to UNIX, Shell scripting, and LaTeX

## README.md File Introduction and Explanation
Before moving into the main content, I would like to briefly introduce the README.md file. This file includes the whole course structure and learning goals of each week, also contains what we did and our understanding of what we did, which is the most important part in this document. 

This README.md file is only for week1 learning and it is inside the week1 folder. Each week will have its own README.md file, which can be easily found in each week’s folder. Alongside these weekly files, there is an overarching README.md file within the course's main directory (CMEECourseWork/), which summarises the whole course structure and main learning goals.

## Week 1 Overview and Purpose
Week 1 indicates the introduction of **UNIX/Linux commands**, **Shell scripting**, **Git version control**, and **LaTeX**, which are foundational computational tools used throughout our CMEE course. The main goal for this week is to gain familiarity with these tools.

##  UNIX and Linux
This is the first part of this week. In this section, we learned to write commands within UNIX/Linux,  and practiced a range of basic terminal commands to make myself be more and more familiar with the terminal (because terminal is quite a new thing to me). The goal for this week was to understand directory structures, file management, command and how to combine commands efficiently using pipes and redirection.

### What I did
We started by understanding the UNIX system and building my CMEECoureseWork/week1 directory with sub-directories (code, data, result and sandbox). Then we learned how to navigate through the file system, use Linux command to create, move and manage files. We also practiced combining commands with pipes and redirection to handle tasks more efficiently.

### FASTA exercise
I used such as `wc`, `tail`, `tr`, `grep`, and `awk` to write five commands, and combined them into **`UnixPrac1.txt`**, located in the `week1/code/` directory:

1. **Count the number of lines in each file** \\

`.wc -l ../data/fasta/*` \\

`.wc` =  word count; `.-l` indicates that we only count lines; `.../data/fasta/*` is to path all the docyments inside the fasta filedirectory. 

2. **Print everything starting from the second line for the E. coli genome** \\

`.tail -n +2 ../data/fasta/E_coli.fasta` \\

`.tail` means we want to print the last part of the document; `.-n +2` means we want to start displaying from line 2 onward; `.../data/fasta/E_coli.fasta` is the path to the target file.

3. **Count the sequence length of this genome** \\

`.tail -n +2 ../data/fasta/E_coli.fasta | tr -d '\n' | wc -m` \\

`.tail -n +2` is same as that in Q2, which means that we want to count from line 2 to the end; `.../data/fasta/E_coli.fasta` is the path to target file; `.|` ends that output to `.tr -d '\n'` which removes all newline characters; `.wc -m` counts all characters.

4. **Count the matches of a particular sequence, “ATGC” in the genome of E. coli** \\

`.tail -n +2 ../data/fasta/E_coli.fasta | tr -d '\n' | grep -o "ATGC" | wc -l` \\

All the first part are the same as above. `.tr -d '\n'` removes all newlines. `.grep -o` "ATGC" searches for every exact match of "ATGC" and prints each match on a new line; `.wc -l` only counts lines.


5. **Compute the (A+T)/(G+C) ratio** \\

`.tail -n +2 ../data/fasta/E_coli.fasta | tr -d '\n' | \` \\

awk '{A=gsub(/A/,""); T=gsub(/T/,""); G=gsub(/G/,""); C=gsub(/C/,""); print (A+T)/(G+C)}' \\

All the first part are the same as above. `.tr -d '\n'` removes all newlines. awk command: `.gsub(/A/,"")` counts how many A bases appear, other letters are same way. print (A+T)/(G+C) calculates the ratio of (A+T) to (G+C) bases.

## Shell scripting
In this section, we learned how to write and run bash shell scripts to automate repetitive tasks. We learned the structure and syntax of a shell script ad create seveal shell scripts which were saved in the `code/` directory.

### What I did
I wrote several shell scripts following the instructions in the book. And I would like to introduces them with their functions:

1. **boilerplate.sh** 

This ia a simple starting template for shell script template with author information, date (I put my information into this shell script), and a short description. When bash it, it shows: This is a shell script! 

2. **variables.sh**
This is a shell script shows the use of special variables in bash(such as $0, $1, $#, $@) and user-defined variables (like MY_VAR='some string'). We can input some numbers and carry out some simple mathematical operations.

3. **tabtocsv.sh**
Turns a tab-delimited text file into a comma-separated `.csv` file using the `tr` command. The new file is saved in the same folder with `.csv` added to the name. 

4. **csvtospace.sh**
Replace commas with spaces in the `.csv` file. It checks for errors (such as missing inputs) and saves the new output file without overwriting the original file.

5. **CountLines.sh**
`.wl -l` count only lines of the targeted file. And, outputs the filenames and line count to the terminal.

6. **ConcatenateTwoFiles.sh**
ombines the contents of two files into a third one using `cat`. 

7. **tiff2png.sh**
Converts all `.tif` image files in the current folder into `.png` format using ImageMagick’s `convert` command. Uses a simple `for` loop. 

8. **CompileLaTeX.sh**
This shell script contains one-line UNIX commands used for the FASTA file exercise (counting lines, sequence length, motifs, and base composition). 

## Version Control with Git
This section introduced **Git** as a version control for tracking changes of the code and files, then managing collaborative work. 

### What we did
First, we learnt how to install Git though the terminal for version control, and then setting up our username and university email address. Then, I initialised a local repository. After that, I created an SSH connection though terminal linking the local repository to GitHub. Next, I practised creating and merging branches to safely test new code, configured the `.gitignore` file to exclude non-essential files such as logs and backups, and wrote a README.md file describing the first week's content.

## LaTeX
In this section, we were introduced to LaTex, but I used LaTex a lot when I was in my undergraduate degree. So this section is quite simple for me.

### What we did
I installed LaTex though terminal. Then I created the document **FirstExample.tex** with a title, abstract, sections, equations and references. Added a bibliography file **FirstBiblio,bib**. Then compiled the document and produced a fully LaTex **.pdf** document.



