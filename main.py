from pet import Pet

def main():
    # Create a new pet
    my_pet = Pet("Fluffy")
    
    # Display initial status
    my_pet.get_status()
    
    # Test eating
    print("\nTesting eat() method:")
    my_pet.eat()
    my_pet.get_status()
    
    # Test playing
    print("\nTesting play() method:")
    my_pet.play()
    my_pet.get_status()
    
    # Test sleeping
    print("\nTesting sleep() method:")
    my_pet.sleep()
    my_pet.get_status()
    
    # Test training
    print("\nTesting training:")
    my_pet.train("sit")
    my_pet.train("roll over")
    my_pet.train("fetch")
    my_pet.show_tricks()
    
    # Try to teach the same trick again
    print("\nTrying to teach the same trick:")
    my_pet.train("sit")
    
    # Test playing when tired
    print("\nTesting play when tired:")
    for _ in range(3):
        my_pet.play()
    my_pet.get_status()
    
    # Restore energy with sleep
    print("\nRestoring energy:")
    my_pet.sleep()
    my_pet.get_status()

if __name__ == "__main__":
    main()
