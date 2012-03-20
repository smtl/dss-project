
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
   enum yy_linktokentype {
     INPUT = 286,
     OUTPUT = 287,
     ID = 284,
     AND = 274,
     DOT = 282
   };
#endif
/* Tokens.  */
#define INPUT 286
#define OUTPUT 287
#define ID 284
#define AND 274
#define DOT 282




#if ! defined YY_LINK_STYPE_TYPE && ! defined YY_LINK_STYPE_TYPE_IS_DECLARED
typedef union YY_LINK_STYPE_TYPE
{

/* Line 1676 of yacc.c  */
#line 33 "link_parser.y"

  struct tree *tree;
  char   *string;



/* Line 1676 of yacc.c  */
#line 73 "y.tab.h"
} YY_LINK_STYPE_TYPE;
# define YY_LINK_STYPE_TYPE_IS_TRIVIAL 1
# define yy_linkstype YY_LINK_STYPE_TYPE /* obsolescent; will be withdrawn */
# define YY_LINK_STYPE_TYPE_IS_DECLARED 1
#endif

extern YY_LINK_STYPE_TYPE yy_linklval;


