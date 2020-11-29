#! /bin/bash -
if [[ ! -e "input/day_$1.txt" ]]; then
    touch "input/day_$1.txt"
fi

if [[ ! -e "day_$1.py" ]]; then
    touch "day_$1.py"
    cat solution-template.py >> "day_$1.py"
fi