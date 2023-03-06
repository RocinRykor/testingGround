from sheaf_generator import security_sheaf

if __name__ == '__main__':
    test = security_sheaf.generate_sheaf(3, 11)

    print("Printing Sheaf!  (Step: Event)")
    for step in test:
        print(step)
