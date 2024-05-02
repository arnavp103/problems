#!/usr/bin/env fish

# Sample usage:
# `./new_problem.fish "557. Two Sum" sql`
# creates a file named e.g. 557.sql
# appends 557 Two sum


function new_problem
	set -l num (echo $argv[1] | cut -d' ' -f1)
	set -l name (echo $argv[1] | cut -d' ' -f2-)
	# remove trailing dot from num
	set -l num (echo $num | tr -d .)
	set -l ext $argv[2]
	echo "Creating $num.$ext $name"
	set -l filename "$num.$ext"
	touch $filename
	echo "$num $name" >> $filename
	echo "Created $filename"
end

new_problem $argv

