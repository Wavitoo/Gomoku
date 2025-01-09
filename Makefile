##
## EPITECH PROJECT, 2024
## Makefile
## File description:
## Makefile
##

MAIN = 			src/main.py

SRC		= 		$(MAIN)\
				src/Gomoku.py\
				src/AI.py\
				src/gomoku_board_eval.py\
				src/Algo.py\
				src/commands/\

NAME	=		pbrain-gomoku-ai

all: $(NAME)

$(NAME):
	cp -r $(SRC) .
	mv main.py $(NAME)
	chmod +x $(NAME)

clean:
	$(RM) -r __pycache__

fclean: clean
	$(RM) $(NAME)
	rm -rf Gomoku.py AI.py main.py gomoku_board_eval.py commands/ Algo.py

re: fclean all

.PHONY: all clean fclean re
