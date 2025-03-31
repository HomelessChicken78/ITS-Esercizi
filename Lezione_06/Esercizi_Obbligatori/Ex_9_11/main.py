from users import *

me: User = User("Cristiano", "Coccia", "HomelessChicken78", "c.coccia@its-ictacademy.com")
p1: Privileges = Privileges(["Mute", "Kick", "Ban", "Accept", "Invite", "Add"])
adm1: Admin = Admin(me, p1)

adm1.user.describe_user()
adm1.priv.show_privileges()