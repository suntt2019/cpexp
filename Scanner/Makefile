SHELL := /bin/bash

name = Testlex
antlr4 = java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:${CLASSPATH}" org.antlr.v4.Tool
grun = java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:${CLASSPATH}" org.antlr.v4.gui.TestRig

passed_cnt = 0

build/Testlex.class: Testlex.g4
	mkdir -p build
	$(antlr4) $(name).g4 -o build
	javac build/*.java

clean:
	rm -r build || :
	rm tests/*.actual tests/*.diff || :
all: build/Testlex.class
run:
	cd build && $(grun) $(name) tokens -tokens
check: build/Testlex.class
	@echo 'Executing checks:'
	@cd build && for filename in $(shell ls tests) ; do \
		name="$${filename%.*}"; \
		extension="$${filename##*.}"; \
		if [ $${extension} = "in" ]; then \
			$(grun) $(name) tokens -tokens ../tests/$${filename} > ../tests/$${name}.actual; \
			diff ../tests/$${name}.actual ../tests/$${name}.expected > ../tests/$${name}.diff && echo ' ** pass' $${name} || echo ' ** FAILED' $${name}; \
		fi; \
	done

#tests/example.diff: build/Testlex.class tests/example.in tests/example.expected
#	@cd build && $(grun) $(name) tokens -tokens ../tests/example.in > ../tests/example.actual
#	@diff tests/example.actual tests/example.expected > tests/example.diff
#check: build/Testlex.class tests/example.diff
#	@ [ -s tests/example.diff ] && echo '** test' example 'passed.' || echo '** test' example 'FAILED.'
