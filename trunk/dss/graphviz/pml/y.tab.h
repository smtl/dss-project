
/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton interface for Bison's Yacc-like parsers in C
   
      Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     ACTION = 258,
     AGENT = 259,
     BRANCH = 260,
     CREATES = 261,
     EXECUTABLE = 262,
     INPUT = 263,
     ITERATION = 264,
     MANUAL = 265,
     OUTPUT = 266,
     PROCESS = 267,
     PROVIDES = 268,
     REQUIRES = 269,
     SCRIPT = 270,
     SELECTION = 271,
     SEQUENCE = 272,
     TOOL = 273,
     OR = 274,
     AND = 275,
     EQ = 276,
     NE = 277,
     LE = 278,
     GE = 279,
     LT = 280,
     GT = 281,
     NOT = 282,
     DOT = 283,
     QUALIFIER = 284,
     ID = 285,
     NUMBER = 286,
     STRING = 287,
     JOIN = 288,
     RENDEZVOUS = 289
   };
#endif
/* Tokens.  */
#define ACTION 258
#define AGENT 259
#define BRANCH 260
#define CREATES 261
#define EXECUTABLE 262
#define INPUT 263
#define ITERATION 264
#define MANUAL 265
#define OUTPUT 266
#define PROCESS 267
#define PROVIDES 268
#define REQUIRES 269
#define SCRIPT 270
#define SELECTION 271
#define SEQUENCE 272
#define TOOL 273
#define OR 274
#define AND 275
#define EQ 276
#define NE 277
#define LE 278
#define GE 279
#define LT 280
#define GT 281
#define NOT 282
#define DOT 283
#define QUALIFIER 284
#define ID 285
#define NUMBER 286
#define STRING 287
#define JOIN 288
#define RENDEZVOUS 289




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
{

/* Line 1676 of yacc.c  */
#line 38 "parser.y"

    int           val;
    struct tree  *tree;
    struct graph *graph;
    char         *string;



/* Line 1676 of yacc.c  */
#line 129 "y.tab.h"
} YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;


