#!/bin/bash

# Ask the user for input
read -p "Please enter your name: " name
read -p "Please enter your age: " age
read -p "Please enter your favorite programming language: " favorite_language
read -p "Please enter your hobby: " hobby

# Print a formatted summary
echo ""
echo "Hello $name!"
echo "You are: $age years old."
echo "Your favorite programming language is $favorite_language and your hobby is $hobby."
