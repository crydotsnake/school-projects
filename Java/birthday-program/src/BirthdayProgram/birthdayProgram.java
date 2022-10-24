package BirthdayProgram;

import java.util.Scanner;

public class birthdayProgram {
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		String name;
		System.out.println("Please enter your name:");
		name = sc.next();

		// Calculates the year of birth and asks you if you already had birthday this year
		int age;
		int thisYear = 2022;
		int birthYear = 2001;
		System.out.println("Please enter your year of birth:");
		birthYear = sc.nextInt();

		System.out.println("Do you already had birthday this year? 1: Yes, 2: no");
		int choice = sc.nextInt();
		
		if (choice == 1) {
			age = thisYear - birthYear;
			System.out.println("Hello " + name + "," + " you are " + age +  " years old");
		} else {
			age = thisYear - birthYear - 1;
			System.out.println("Hello " + name + "," + " you are still " + age +  " years old");
		}
		sc.close();
	}
}
