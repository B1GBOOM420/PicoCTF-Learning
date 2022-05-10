 #!/usr/bin/bash

python3 fixme1.py | grep -oE "picoCTF{.*}" --color=none
