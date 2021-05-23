from oop_inheritance import Parents, Child

boy = Child("Shiva", "Parvathy", "Murugan")
boy.get_father_name()  # method inherited from Parents class
boy.get_mother_name()  # method inherited from Parents Class
boy.get_parents_info()  # child class method that uses attributes from Parents class
boy.get_location()

parent = Parents("Shiva", "Parvathi")
parent.get_location()
