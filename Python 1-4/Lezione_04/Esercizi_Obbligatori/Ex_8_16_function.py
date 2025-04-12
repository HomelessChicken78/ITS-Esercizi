def describe_city(name: str = "Rome", country: str = "Italy") -> None:
    print(f"The city \"{name}\" is situated in {country}")

if __name__ == "__main__":
    describe_city()
    print("----------------------------")
    describe_city("Barcelona", "Spain")
    print("----------------------------")
    describe_city("Paris", "France")