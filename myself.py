import textwrap

name = "Tanishq Chauhan"
interests = ["Web Development", "AI", "ML"]
skills = ["Web development", "WordPress", "Python"]

introduction = f"""
Hi, I'm {name}.

I'm passionate about:
{", ".join(textwrap.wrap(', '.join(interests), width=30))}

I'm also skilled in:
{", ".join(textwrap.wrap(', '.join(skills), width=30))}

It's a pleasure to meet you!
"""

print("=" * 50)
print(introduction)
print("=" * 50)