package main

import (
	"fmt"
)

func main() {

	var name string
	var thisYear int
	var birthYear int
	var choice string

	fmt.Println("Please enter your name:")
	fmt.Scan(&name)
	fmt.Println("Please enter your year of birth")
	fmt.Scan(&birthYear)
	fmt.Println("Please specify this year")
	fmt.Scan(&thisYear)
	fmt.Println("Do you already had birthday this year? Y/N")
	fmt.Scan(&choice)

	if choice == "Y" {
		age := thisYear - birthYear
		fmt.Printf(fmt.Sprintf("Hello %v, you are %v years old", name, age))
	} else {
		age := thisYear - birthYear - 1
		fmt.Printf(fmt.Sprintf("Hello %v, you are still %v years old", name, age))
	}

	fmt.Println()
	var askAgainMessage string
	fmt.Println("Would you like to ask another person? Y/N")
	fmt.Scan(&askAgainMessage)

	if askAgainMessage == "Y" {
		main()
	} else {
		fmt.Printf("Good bye !")
	}
}