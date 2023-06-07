// ------------------------------------ //
//
//  Interface -- Implementation
//
// ------------------------------------ //

/*
Interfaces are implemented implicitly.

A type never declares that it implements a given interface. If an interface exists and a type has the proper methods defined, 
then the type automatically fulfills that interface.

*/

// ------------------------- //
//  Assignment -- Practice
// ------------------------- //

/*
At Textio we have full-time employees and contract employees. We have been tasked with making a more general employee interface 
so that dealing with different employee types is simpler.

Add the missing getSalary method to the contractor type so that it fulfills the employee interface.

A contractor's salary is their hourly pay multiplied by how many hours they work per year.

*/

package main

import (
	"fmt"
)

type employee interface {
	getName() string
	getSalary() int
}

type contractor struct {
	name         string
	hourlyPay    int
	hoursPerYear int
}

func (c contractor) getName() string {
	return c.name
}

func (gs contractor) getSalary() int {
	return gs.hourlyPay * gs.hoursPerYear
} 

// don't touch below this line

type fullTime struct {
	name   string
	salary int
}

func (ft fullTime) getSalary() int {
	return ft.salary
}

func (ft fullTime) getName() string {
	return ft.name
}

func test(e employee) {
	fmt.Println(e.getName(), e.getSalary())
	fmt.Println("====================================")
}

func main() {
	test(fullTime{
		name:   "Jack",
		salary: 50000,
	})
	test(contractor{
		name:         "Bob",
		hourlyPay:    100,
		hoursPerYear: 73,
	})
	test(contractor{
		name:         "Jill",
		hourlyPay:    872,
		hoursPerYear: 982,
	})
}

// ------------------------- //
// How is an interface fulfilled?
// ------------------------- //

// Initial
// A type has all the required interface's methods defined on it

/*
A type implements an interface by implementing its methods. Unlike in many other languages, there is no explicit declaration of intent, there is no "implements" keyword.

Implicit interfaces decouple the definition of an interface from its implementation. You may add methods to a type and in the process be unknowingly implementing various interfaces, and that's okay.

*/