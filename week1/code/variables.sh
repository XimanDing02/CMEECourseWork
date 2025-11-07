#!/bin/sh

## Illustrates the use of variables 

# Special variables
echo "This script was called with $# parameters"
echo "The script's name is $0"
echo "The arguments are $@"
echo "The first argument is $1"
echo "The second argument is $2"

# Assigned Variables; Explicit declaration:
MY_VAR='some string' 
echo "The current value of the variable is: $MY_VAR"
echo
echo "Please enter a new string (or press Enter to keep the same):"
read NEW_VAR

# If no new content is entered, retain the original value.
if [ -n "$NEW_VAR" ]; then
    MY_VAR="$NEW_VAR"
fi

echo
echo "The current value of the variable is: $MY_VAR"
echo

## Assigned Variables; Reading (multiple values) from user input:
echo "Enter two numbers separated by space(s):"
read a b

# If no value is entered, set the default value.
if [ -z "$a" ] || [ -z "$b" ]; then
    echo "No input detected, using default values 0 and 0."
    a=0
    b=0
fi

echo
echo "You entered $a and $b; their sum is:"

## Assigned Variables; Command substitution
MY_SUM=$(expr $a + $b)
echo "$MY_SUM"