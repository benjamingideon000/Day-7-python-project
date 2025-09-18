#!/bin/bash

# Ask the user for two numbers
read -p "Enter the first number: " num1
read -p "Enter the second number: " num2

# Ask the user for an operator
read -p "Enter the operator (+, -, *, /, %, **): " operator

# Calculate and print the result
case $operator in
  "+")
    result=$(echo "scale=2; $num1 + $num2" | bc)
    echo "$num1 + $num2 = $result"
    ;;
  "-")
    result=$(echo "scale=2; $num1 - $num2" | bc)
    echo "$num1 - $num2 = $result"
    ;;
  "*")
    result=$(echo "scale=2; $num1 * $num2" | bc)
    echo "$num1 * $num2 = $result"
    ;;
  "/")
    if [ $num2 != 0 ]; then
      result=$(echo "scale=2; $num1 / $num2" | bc)
      echo "$num1 / $num2 = $result"
    else
      echo "Error: Division by zero is not allowed."
    fi
    ;;
  "%")
    if [ $num2 != 0 ]; then
      result=$(echo "$num1 % $num2" | bc)
      echo "$num1 % $num2 = $result"
    else
      echo "Error: Division by zero is not allowed."
    fi
    ;;
  "**")
    result=$(echo "scale=2; $num1 ^ $num2" | bc -l)
    echo "$num1 ** $num2 = $result"
    ;;
  *)
    echo "Error: Invalid operator."
    ;;
esac
