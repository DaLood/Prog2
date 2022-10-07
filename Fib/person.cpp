#include <cstdlib>
// Person class 

class Person{
	public:
    		Person(int);
    		int get();
    		void set(int);
    		int fib();

	private:
    		int age;
    		int prev;
    		int curr;
    		int next;
	};

Person::Person(int n){
	age = n;
	}

int Person::get(){
	return age;
	}

void Person::set(int n){
	age = n;
	}	


int Person::fib(){
	prev = 1;
	curr = 1;
	next = 1;

	for (int i = 3; i <= age; ++i){
       		next = curr + prev;
        	prev = curr;
        	curr = next;
    	}
    	return next;
	}
	


extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	
	int Person_fib(Person* person) {return person->fib();}


	void Person_set(Person* person, int n) {person->set(n);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}

