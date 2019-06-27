# -*- coding: utf-8 -*-
import re

title = "asdf胜多负少！asdf12a1$s,3啊1fg"
t = re.sub(r"\W", "@", title)
print(t)
