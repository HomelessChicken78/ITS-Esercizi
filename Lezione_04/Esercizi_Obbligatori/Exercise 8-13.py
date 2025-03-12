'''8-13. User Profile:
Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.
All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"'''

def build_profile(**kwargs) -> str:
    profile: str = ""
    for k, w in kwargs.items():
        profile += k + " : " + w + ", "
    return profile

#Output Check
print(build_profile(name="Cristiano Coccia", age="20", height="1.58"))