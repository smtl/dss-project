
/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton implementation for Bison's Yacc-like parsers in C
   
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

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy_link or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "2.4.1"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1

/* Using locations.  */
#define YYLSP_NEEDED 0



/* Copy the first part of user declarations.  */

/* Line 189 of yacc.c  */
#line 1 "link_parser.y"

/************************************************************************
 * File:        parser.y                                                *
 *                                                                      *
 * Description:	This file contains the yacc specification for the       *
 *		        parser.                                         *
 ************************************************************************/

# include "lexer.h"
# include "link_parser.h"

/* Public variable definitions */

Tree inputs;
Tree outputs;

/* Private function declarations */

static void and_trees (
# ifdef ANSI_PROTOTYPES
    Tree *		/* ptr  */,
    Tree		/* tree */
# endif
);



/* Line 189 of yacc.c  */
#line 101 "y.tab.c"

/* Enabling traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif

/* Enabling the token table.  */
#ifndef YYTOKEN_TABLE
# define YYTOKEN_TABLE 0
#endif


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

/* Line 214 of yacc.c  */
#line 33 "link_parser.y"

  struct tree *tree;
  char   *string;



/* Line 214 of yacc.c  */
#line 158 "y.tab.c"
} YY_LINK_STYPE_TYPE;
# define YY_LINK_STYPE_TYPE_IS_TRIVIAL 1
# define yy_linkstype YY_LINK_STYPE_TYPE /* obsolescent; will be withdrawn */
# define YY_LINK_STYPE_TYPE_IS_DECLARED 1
#endif


/* Copy the second part of user declarations.  */


/* Line 264 of yacc.c  */
#line 170 "y.tab.c"

#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yy_linktype_uint8;
#else
typedef unsigned char yy_linktype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yy_linktype_int8;
#elif (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
typedef signed char yy_linktype_int8;
#else
typedef short int yy_linktype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yy_linktype_uint16;
#else
typedef unsigned short int yy_linktype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yy_linktype_int16;
#else
typedef short int yy_linktype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned int
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(msgid) dgettext ("bison-runtime", msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(msgid) msgid
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(e) ((void) (e))
#else
# define YYUSE(e) /* empty */
#endif

/* Identity function, used to suppress warnings about constant conditions.  */
#ifndef lint
# define YYID(n) (n)
#else
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static int
YYID (int yy_linki)
#else
static int
YYID (yy_linki)
    int yy_linki;
#endif
{
  return yy_linki;
}
#endif

#if ! defined yy_linkoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#     ifndef _STDLIB_H
#      define _STDLIB_H 1
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's `empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (YYID (0))
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined _STDLIB_H \
       && ! ((defined YYMALLOC || defined malloc) \
	     && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef _STDLIB_H
#    define _STDLIB_H 1
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yy_linkoverflow || YYERROR_VERBOSE */


#if (! defined yy_linkoverflow \
     && (! defined __cplusplus \
	 || (defined YY_LINK_STYPE_TYPE_IS_TRIVIAL && YY_LINK_STYPE_TYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yy_linkalloc
{
  yy_linktype_int16 yy_linkss_alloc;
  YY_LINK_STYPE_TYPE yy_linkvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yy_linkalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yy_linktype_int16) + sizeof (YY_LINK_STYPE_TYPE)) \
      + YYSTACK_GAP_MAXIMUM)

/* Copy COUNT objects from FROM to TO.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(To, From, Count) \
      __builtin_memcpy (To, From, (Count) * sizeof (*(From)))
#  else
#   define YYCOPY(To, From, Count)		\
      do					\
	{					\
	  YYSIZE_T yy_linki;				\
	  for (yy_linki = 0; yy_linki < (Count); yy_linki++)	\
	    (To)[yy_linki] = (From)[yy_linki];		\
	}					\
      while (YYID (0))
#  endif
# endif

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)				\
    do									\
      {									\
	YYSIZE_T yy_linknewbytes;						\
	YYCOPY (&yy_linkptr->Stack_alloc, Stack, yy_linksize);			\
	Stack = &yy_linkptr->Stack_alloc;					\
	yy_linknewbytes = yy_linkstacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
	yy_linkptr += yy_linknewbytes / sizeof (*yy_linkptr);				\
      }									\
    while (YYID (0))

#endif

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  2
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   13

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  11
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  7
/* YYNRULES -- Number of rules.  */
#define YYNRULES  11
/* YYNRULES -- Number of states.  */
#define YYNSTATES  20

/* YYTRANSLATE(YYLEX) -- Bison symbol number corresponding to YYLEX.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   287

#define YYTRANSLATE(YYX)						\
  ((unsigned int) (YYX) <= YYMAXUTOK ? yy_linktranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[YYLEX] -- Bison symbol number corresponding to YYLEX.  */
static const yy_linktype_uint8 yy_linktranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,    10,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     8,     2,     9,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     6,     2,     2,     2,     2,     2,
       2,     2,     7,     2,     5,     2,     3,     4
};

#if YYDEBUG
/* YYPRHS[YYN] -- Index of the first RHS symbol of rule number YYN in
   YYRHS.  */
static const yy_linktype_uint8 yy_linkprhs[] =
{
       0,     0,     3,     6,     7,    12,    17,    19,    23,    25,
      27,    31
};

/* YYRHS -- A `-1'-separated list of the rules' RHS.  */
static const yy_linktype_int8 yy_linkrhs[] =
{
      12,     0,    -1,    12,    13,    -1,    -1,     3,     8,    14,
       9,    -1,     4,     8,    14,     9,    -1,    15,    -1,    14,
      10,    15,    -1,    16,    -1,    17,    -1,    17,     7,    17,
      -1,     5,    -1
};

/* YYRLINE[YYN] -- source line where rule number YYN was defined.  */
static const yy_linktype_uint8 yy_linkrline[] =
{
       0,    50,    50,    51,    55,    59,    66,    67,    74,    75,
      79,    86
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || YYTOKEN_TABLE
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yy_linktname[] =
{
  "$end", "error", "$undefined", "INPUT", "OUTPUT", "ID", "AND", "DOT",
  "'{'", "'}'", "'&'", "$accept", "specification_list", "specification",
  "resource_list", "resource", "attributed_resource", "identifier", 0
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[YYLEX-NUM] -- Internal token number corresponding to
   token YYLEX-NUM.  */
static const yy_linktype_uint16 yy_linktoknum[] =
{
       0,   256,   285,   286,   287,   284,   274,   282,   123,   125,
      38
};
# endif

/* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yy_linktype_uint8 yy_linkr1[] =
{
       0,    11,    12,    12,    13,    13,    14,    14,    15,    15,
      16,    17
};

/* YYR2[YYN] -- Number of symbols composing right hand side of rule YYN.  */
static const yy_linktype_uint8 yy_linkr2[] =
{
       0,     2,     2,     0,     4,     4,     1,     3,     1,     1,
       3,     1
};

/* YYDEFACT[STATE-NAME] -- Default rule to reduce with in state
   STATE-NUM when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yy_linktype_uint8 yy_linkdefact[] =
{
       3,     0,     1,     0,     0,     2,     0,     0,    11,     0,
       6,     8,     9,     0,     4,     0,     0,     5,     7,    10
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yy_linktype_int8 yy_linkdefgoto[] =
{
      -1,     1,     5,     9,    10,    11,    12
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -9
static const yy_linktype_int8 yy_linkpact[] =
{
      -9,     0,    -9,    -1,     1,    -9,     3,     3,    -9,    -8,
      -9,    -9,     4,    -4,    -9,     3,     3,    -9,    -9,    -9
};

/* YYPGOTO[NTERM-NUM].  */
static const yy_linktype_int8 yy_linkpgoto[] =
{
      -9,    -9,    -9,     5,    -5,    -9,    -3
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -1
static const yy_linktype_uint8 yy_linktable[] =
{
       2,    14,    15,     3,     4,    17,    15,     6,     8,     7,
      18,    16,    13,    19
};

static const yy_linktype_uint8 yy_linkcheck[] =
{
       0,     9,    10,     3,     4,     9,    10,     8,     5,     8,
      15,     7,     7,    16
};

/* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
   symbol of state STATE-NUM.  */
static const yy_linktype_uint8 yy_linkstos[] =
{
       0,    12,     0,     3,     4,    13,     8,     8,     5,    14,
      15,    16,    17,    14,     9,    10,     7,     9,    15,    17
};

#define yy_linkerrok		(yy_linkerrstatus = 0)
#define yy_linkclearin	(yy_linkchar = YYEMPTY)
#define YYEMPTY		(-2)
#define YYEOF		0

#define YYACCEPT	goto yy_linkacceptlab
#define YYABORT		goto yy_linkabortlab
#define YYERROR		goto yy_linkerrorlab


/* Like YYERROR except do call yy_linkerror.  This remains here temporarily
   to ease the transition to the new meaning of YYERROR, for GCC.
   Once GCC version 2 has supplanted version 1, this can go.  */

#define YYFAIL		goto yy_linkerrlab

#define YYRECOVERING()  (!!yy_linkerrstatus)

#define YYBACKUP(Token, Value)					\
do								\
  if (yy_linkchar == YYEMPTY && yy_linklen == 1)				\
    {								\
      yy_linkchar = (Token);						\
      yy_linklval = (Value);						\
      yy_linktoken = YYTRANSLATE (yy_linkchar);				\
      YYPOPSTACK (1);						\
      goto yy_linkbackup;						\
    }								\
  else								\
    {								\
      yy_linkerror (YY_("syntax error: cannot back up")); \
      YYERROR;							\
    }								\
while (YYID (0))


#define YYTERROR	1
#define YYERRCODE	256


/* YYLLOC_DEFAULT -- Set CURRENT to span from RHS[1] to RHS[N].
   If N is 0, then set CURRENT to the empty location which ends
   the previous symbol: RHS[0] (always defined).  */

#define YYRHSLOC(Rhs, K) ((Rhs)[K])
#ifndef YYLLOC_DEFAULT
# define YYLLOC_DEFAULT(Current, Rhs, N)				\
    do									\
      if (YYID (N))                                                    \
	{								\
	  (Current).first_line   = YYRHSLOC (Rhs, 1).first_line;	\
	  (Current).first_column = YYRHSLOC (Rhs, 1).first_column;	\
	  (Current).last_line    = YYRHSLOC (Rhs, N).last_line;		\
	  (Current).last_column  = YYRHSLOC (Rhs, N).last_column;	\
	}								\
      else								\
	{								\
	  (Current).first_line   = (Current).last_line   =		\
	    YYRHSLOC (Rhs, 0).last_line;				\
	  (Current).first_column = (Current).last_column =		\
	    YYRHSLOC (Rhs, 0).last_column;				\
	}								\
    while (YYID (0))
#endif


/* YY_LOCATION_PRINT -- Print the location on the stream.
   This macro was not mandated originally: define only if we know
   we won't break user code: when these are the locations we know.  */

#ifndef YY_LOCATION_PRINT
# if YYLTYPE_IS_TRIVIAL
#  define YY_LOCATION_PRINT(File, Loc)			\
     fprintf (File, "%d.%d-%d.%d",			\
	      (Loc).first_line, (Loc).first_column,	\
	      (Loc).last_line,  (Loc).last_column)
# else
#  define YY_LOCATION_PRINT(File, Loc) ((void) 0)
# endif
#endif


/* YYLEX -- calling `yy_linklex' with the right arguments.  */

#ifdef YYLEX_PARAM
# define YYLEX yy_linklex (YYLEX_PARAM)
#else
# define YYLEX yy_linklex ()
#endif

/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)			\
do {						\
  if (yy_linkdebug)					\
    YYFPRINTF Args;				\
} while (YYID (0))

# define YY_SYMBOL_PRINT(Title, Type, Value, Location)			  \
do {									  \
  if (yy_linkdebug)								  \
    {									  \
      YYFPRINTF (stderr, "%s ", Title);					  \
      yy_link_symbol_print (stderr,						  \
		  Type, Value); \
      YYFPRINTF (stderr, "\n");						  \
    }									  \
} while (YYID (0))


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

/*ARGSUSED*/
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_link_symbol_value_print (FILE *yy_linkoutput, int yy_linktype, YY_LINK_STYPE_TYPE const * const yy_linkvaluep)
#else
static void
yy_link_symbol_value_print (yy_linkoutput, yy_linktype, yy_linkvaluep)
    FILE *yy_linkoutput;
    int yy_linktype;
    YY_LINK_STYPE_TYPE const * const yy_linkvaluep;
#endif
{
  if (!yy_linkvaluep)
    return;
# ifdef YYPRINT
  if (yy_linktype < YYNTOKENS)
    YYPRINT (yy_linkoutput, yy_linktoknum[yy_linktype], *yy_linkvaluep);
# else
  YYUSE (yy_linkoutput);
# endif
  switch (yy_linktype)
    {
      default:
	break;
    }
}


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_link_symbol_print (FILE *yy_linkoutput, int yy_linktype, YY_LINK_STYPE_TYPE const * const yy_linkvaluep)
#else
static void
yy_link_symbol_print (yy_linkoutput, yy_linktype, yy_linkvaluep)
    FILE *yy_linkoutput;
    int yy_linktype;
    YY_LINK_STYPE_TYPE const * const yy_linkvaluep;
#endif
{
  if (yy_linktype < YYNTOKENS)
    YYFPRINTF (yy_linkoutput, "token %s (", yy_linktname[yy_linktype]);
  else
    YYFPRINTF (yy_linkoutput, "nterm %s (", yy_linktname[yy_linktype]);

  yy_link_symbol_value_print (yy_linkoutput, yy_linktype, yy_linkvaluep);
  YYFPRINTF (yy_linkoutput, ")");
}

/*------------------------------------------------------------------.
| yy_link_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_link_stack_print (yy_linktype_int16 *yy_linkbottom, yy_linktype_int16 *yy_linktop)
#else
static void
yy_link_stack_print (yy_linkbottom, yy_linktop)
    yy_linktype_int16 *yy_linkbottom;
    yy_linktype_int16 *yy_linktop;
#endif
{
  YYFPRINTF (stderr, "Stack now");
  for (; yy_linkbottom <= yy_linktop; yy_linkbottom++)
    {
      int yy_linkbot = *yy_linkbottom;
      YYFPRINTF (stderr, " %d", yy_linkbot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)				\
do {								\
  if (yy_linkdebug)							\
    yy_link_stack_print ((Bottom), (Top));				\
} while (YYID (0))


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_link_reduce_print (YY_LINK_STYPE_TYPE *yy_linkvsp, int yy_linkrule)
#else
static void
yy_link_reduce_print (yy_linkvsp, yy_linkrule)
    YY_LINK_STYPE_TYPE *yy_linkvsp;
    int yy_linkrule;
#endif
{
  int yy_linknrhs = yy_linkr2[yy_linkrule];
  int yy_linki;
  unsigned long int yy_linklno = yy_linkrline[yy_linkrule];
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
	     yy_linkrule - 1, yy_linklno);
  /* The symbols being reduced.  */
  for (yy_linki = 0; yy_linki < yy_linknrhs; yy_linki++)
    {
      YYFPRINTF (stderr, "   $%d = ", yy_linki + 1);
      yy_link_symbol_print (stderr, yy_linkrhs[yy_linkprhs[yy_linkrule] + yy_linki],
		       &(yy_linkvsp[(yy_linki + 1) - (yy_linknrhs)])
		       		       );
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)		\
do {					\
  if (yy_linkdebug)				\
    yy_link_reduce_print (yy_linkvsp, Rule); \
} while (YYID (0))

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yy_linkdebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef	YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif



#if YYERROR_VERBOSE

# ifndef yy_linkstrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yy_linkstrlen strlen
#  else
/* Return the length of YYSTR.  */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static YYSIZE_T
yy_linkstrlen (const char *yy_linkstr)
#else
static YYSIZE_T
yy_linkstrlen (yy_linkstr)
    const char *yy_linkstr;
#endif
{
  YYSIZE_T yy_linklen;
  for (yy_linklen = 0; yy_linkstr[yy_linklen]; yy_linklen++)
    continue;
  return yy_linklen;
}
#  endif
# endif

# ifndef yy_linkstpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yy_linkstpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static char *
yy_linkstpcpy (char *yy_linkdest, const char *yy_linksrc)
#else
static char *
yy_linkstpcpy (yy_linkdest, yy_linksrc)
    char *yy_linkdest;
    const char *yy_linksrc;
#endif
{
  char *yy_linkd = yy_linkdest;
  const char *yy_links = yy_linksrc;

  while ((*yy_linkd++ = *yy_links++) != '\0')
    continue;

  return yy_linkd - 1;
}
#  endif
# endif

# ifndef yy_linktnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yy_linkerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yy_linktname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yy_linktnamerr (char *yy_linkres, const char *yy_linkstr)
{
  if (*yy_linkstr == '"')
    {
      YYSIZE_T yy_linkn = 0;
      char const *yy_linkp = yy_linkstr;

      for (;;)
	switch (*++yy_linkp)
	  {
	  case '\'':
	  case ',':
	    goto do_not_strip_quotes;

	  case '\\':
	    if (*++yy_linkp != '\\')
	      goto do_not_strip_quotes;
	    /* Fall through.  */
	  default:
	    if (yy_linkres)
	      yy_linkres[yy_linkn] = *yy_linkp;
	    yy_linkn++;
	    break;

	  case '"':
	    if (yy_linkres)
	      yy_linkres[yy_linkn] = '\0';
	    return yy_linkn;
	  }
    do_not_strip_quotes: ;
    }

  if (! yy_linkres)
    return yy_linkstrlen (yy_linkstr);

  return yy_linkstpcpy (yy_linkres, yy_linkstr) - yy_linkres;
}
# endif

/* Copy into YYRESULT an error message about the unexpected token
   YYCHAR while in state YYSTATE.  Return the number of bytes copied,
   including the terminating null byte.  If YYRESULT is null, do not
   copy anything; just return the number of bytes that would be
   copied.  As a special case, return 0 if an ordinary "syntax error"
   message will do.  Return YYSIZE_MAXIMUM if overflow occurs during
   size calculation.  */
static YYSIZE_T
yy_linksyntax_error (char *yy_linkresult, int yy_linkstate, int yy_linkchar)
{
  int yy_linkn = yy_linkpact[yy_linkstate];

  if (! (YYPACT_NINF < yy_linkn && yy_linkn <= YYLAST))
    return 0;
  else
    {
      int yy_linktype = YYTRANSLATE (yy_linkchar);
      YYSIZE_T yy_linksize0 = yy_linktnamerr (0, yy_linktname[yy_linktype]);
      YYSIZE_T yy_linksize = yy_linksize0;
      YYSIZE_T yy_linksize1;
      int yy_linksize_overflow = 0;
      enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
      char const *yy_linkarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
      int yy_linkx;

# if 0
      /* This is so xgettext sees the translatable formats that are
	 constructed on the fly.  */
      YY_("syntax error, unexpected %s");
      YY_("syntax error, unexpected %s, expecting %s");
      YY_("syntax error, unexpected %s, expecting %s or %s");
      YY_("syntax error, unexpected %s, expecting %s or %s or %s");
      YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s");
# endif
      char *yy_linkfmt;
      char const *yy_linkf;
      static char const yy_linkunexpected[] = "syntax error, unexpected %s";
      static char const yy_linkexpecting[] = ", expecting %s";
      static char const yy_linkor[] = " or %s";
      char yy_linkformat[sizeof yy_linkunexpected
		    + sizeof yy_linkexpecting - 1
		    + ((YYERROR_VERBOSE_ARGS_MAXIMUM - 2)
		       * (sizeof yy_linkor - 1))];
      char const *yy_linkprefix = yy_linkexpecting;

      /* Start YYX at -YYN if negative to avoid negative indexes in
	 YYCHECK.  */
      int yy_linkxbegin = yy_linkn < 0 ? -yy_linkn : 0;

      /* Stay within bounds of both yy_linkcheck and yy_linktname.  */
      int yy_linkchecklim = YYLAST - yy_linkn + 1;
      int yy_linkxend = yy_linkchecklim < YYNTOKENS ? yy_linkchecklim : YYNTOKENS;
      int yy_linkcount = 1;

      yy_linkarg[0] = yy_linktname[yy_linktype];
      yy_linkfmt = yy_linkstpcpy (yy_linkformat, yy_linkunexpected);

      for (yy_linkx = yy_linkxbegin; yy_linkx < yy_linkxend; ++yy_linkx)
	if (yy_linkcheck[yy_linkx + yy_linkn] == yy_linkx && yy_linkx != YYTERROR)
	  {
	    if (yy_linkcount == YYERROR_VERBOSE_ARGS_MAXIMUM)
	      {
		yy_linkcount = 1;
		yy_linksize = yy_linksize0;
		yy_linkformat[sizeof yy_linkunexpected - 1] = '\0';
		break;
	      }
	    yy_linkarg[yy_linkcount++] = yy_linktname[yy_linkx];
	    yy_linksize1 = yy_linksize + yy_linktnamerr (0, yy_linktname[yy_linkx]);
	    yy_linksize_overflow |= (yy_linksize1 < yy_linksize);
	    yy_linksize = yy_linksize1;
	    yy_linkfmt = yy_linkstpcpy (yy_linkfmt, yy_linkprefix);
	    yy_linkprefix = yy_linkor;
	  }

      yy_linkf = YY_(yy_linkformat);
      yy_linksize1 = yy_linksize + yy_linkstrlen (yy_linkf);
      yy_linksize_overflow |= (yy_linksize1 < yy_linksize);
      yy_linksize = yy_linksize1;

      if (yy_linksize_overflow)
	return YYSIZE_MAXIMUM;

      if (yy_linkresult)
	{
	  /* Avoid sprintf, as that infringes on the user's name space.
	     Don't have undefined behavior even if the translation
	     produced a string with the wrong number of "%s"s.  */
	  char *yy_linkp = yy_linkresult;
	  int yy_linki = 0;
	  while ((*yy_linkp = *yy_linkf) != '\0')
	    {
	      if (*yy_linkp == '%' && yy_linkf[1] == 's' && yy_linki < yy_linkcount)
		{
		  yy_linkp += yy_linktnamerr (yy_linkp, yy_linkarg[yy_linki++]);
		  yy_linkf += 2;
		}
	      else
		{
		  yy_linkp++;
		  yy_linkf++;
		}
	    }
	}
      return yy_linksize;
    }
}
#endif /* YYERROR_VERBOSE */


/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

/*ARGSUSED*/
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_linkdestruct (const char *yy_linkmsg, int yy_linktype, YY_LINK_STYPE_TYPE *yy_linkvaluep)
#else
static void
yy_linkdestruct (yy_linkmsg, yy_linktype, yy_linkvaluep)
    const char *yy_linkmsg;
    int yy_linktype;
    YY_LINK_STYPE_TYPE *yy_linkvaluep;
#endif
{
  YYUSE (yy_linkvaluep);

  if (!yy_linkmsg)
    yy_linkmsg = "Deleting";
  YY_SYMBOL_PRINT (yy_linkmsg, yy_linktype, yy_linkvaluep, yy_linklocationp);

  switch (yy_linktype)
    {

      default:
	break;
    }
}

/* Prevent warnings from -Wmissing-prototypes.  */
#ifdef YYPARSE_PARAM
#if defined __STDC__ || defined __cplusplus
int yy_linkparse (void *YYPARSE_PARAM);
#else
int yy_linkparse ();
#endif
#else /* ! YYPARSE_PARAM */
#if defined __STDC__ || defined __cplusplus
int yy_linkparse (void);
#else
int yy_linkparse ();
#endif
#endif /* ! YYPARSE_PARAM */


/* The lookahead symbol.  */
int yy_linkchar;

/* The semantic value of the lookahead symbol.  */
YY_LINK_STYPE_TYPE yy_linklval;

/* Number of syntax errors so far.  */
int yy_linknerrs;



/*-------------------------.
| yy_linkparse or yy_linkpush_parse.  |
`-------------------------*/

#ifdef YYPARSE_PARAM
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
int
yy_linkparse (void *YYPARSE_PARAM)
#else
int
yy_linkparse (YYPARSE_PARAM)
    void *YYPARSE_PARAM;
#endif
#else /* ! YYPARSE_PARAM */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
int
yy_linkparse (void)
#else
int
yy_linkparse ()

#endif
#endif
{


    int yy_linkstate;
    /* Number of tokens to shift before error messages enabled.  */
    int yy_linkerrstatus;

    /* The stacks and their tools:
       `yy_linkss': related to states.
       `yy_linkvs': related to semantic values.

       Refer to the stacks thru separate pointers, to allow yy_linkoverflow
       to reallocate them elsewhere.  */

    /* The state stack.  */
    yy_linktype_int16 yy_linkssa[YYINITDEPTH];
    yy_linktype_int16 *yy_linkss;
    yy_linktype_int16 *yy_linkssp;

    /* The semantic value stack.  */
    YY_LINK_STYPE_TYPE yy_linkvsa[YYINITDEPTH];
    YY_LINK_STYPE_TYPE *yy_linkvs;
    YY_LINK_STYPE_TYPE *yy_linkvsp;

    YYSIZE_T yy_linkstacksize;

  int yy_linkn;
  int yy_linkresult;
  /* Lookahead token as an internal (translated) token number.  */
  int yy_linktoken;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YY_LINK_STYPE_TYPE yy_linkval;

#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yy_linkmsgbuf[128];
  char *yy_linkmsg = yy_linkmsgbuf;
  YYSIZE_T yy_linkmsg_alloc = sizeof yy_linkmsgbuf;
#endif

#define YYPOPSTACK(N)   (yy_linkvsp -= (N), yy_linkssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yy_linklen = 0;

  yy_linktoken = 0;
  yy_linkss = yy_linkssa;
  yy_linkvs = yy_linkvsa;
  yy_linkstacksize = YYINITDEPTH;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yy_linkstate = 0;
  yy_linkerrstatus = 0;
  yy_linknerrs = 0;
  yy_linkchar = YYEMPTY; /* Cause a token to be read.  */

  /* Initialize stack pointers.
     Waste one element of value and location stack
     so that they stay on the same level as the state stack.
     The wasted elements are never initialized.  */
  yy_linkssp = yy_linkss;
  yy_linkvsp = yy_linkvs;

  goto yy_linksetstate;

/*------------------------------------------------------------.
| yy_linknewstate -- Push a new state, which is found in yy_linkstate.  |
`------------------------------------------------------------*/
 yy_linknewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yy_linkssp++;

 yy_linksetstate:
  *yy_linkssp = yy_linkstate;

  if (yy_linkss + yy_linkstacksize - 1 <= yy_linkssp)
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yy_linksize = yy_linkssp - yy_linkss + 1;

#ifdef yy_linkoverflow
      {
	/* Give user a chance to reallocate the stack.  Use copies of
	   these so that the &'s don't force the real ones into
	   memory.  */
	YY_LINK_STYPE_TYPE *yy_linkvs1 = yy_linkvs;
	yy_linktype_int16 *yy_linkss1 = yy_linkss;

	/* Each stack pointer address is followed by the size of the
	   data in use in that stack, in bytes.  This used to be a
	   conditional around just the two extra args, but that might
	   be undefined if yy_linkoverflow is a macro.  */
	yy_linkoverflow (YY_("memory exhausted"),
		    &yy_linkss1, yy_linksize * sizeof (*yy_linkssp),
		    &yy_linkvs1, yy_linksize * sizeof (*yy_linkvsp),
		    &yy_linkstacksize);

	yy_linkss = yy_linkss1;
	yy_linkvs = yy_linkvs1;
      }
#else /* no yy_linkoverflow */
# ifndef YYSTACK_RELOCATE
      goto yy_linkexhaustedlab;
# else
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yy_linkstacksize)
	goto yy_linkexhaustedlab;
      yy_linkstacksize *= 2;
      if (YYMAXDEPTH < yy_linkstacksize)
	yy_linkstacksize = YYMAXDEPTH;

      {
	yy_linktype_int16 *yy_linkss1 = yy_linkss;
	union yy_linkalloc *yy_linkptr =
	  (union yy_linkalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yy_linkstacksize));
	if (! yy_linkptr)
	  goto yy_linkexhaustedlab;
	YYSTACK_RELOCATE (yy_linkss_alloc, yy_linkss);
	YYSTACK_RELOCATE (yy_linkvs_alloc, yy_linkvs);
#  undef YYSTACK_RELOCATE
	if (yy_linkss1 != yy_linkssa)
	  YYSTACK_FREE (yy_linkss1);
      }
# endif
#endif /* no yy_linkoverflow */

      yy_linkssp = yy_linkss + yy_linksize - 1;
      yy_linkvsp = yy_linkvs + yy_linksize - 1;

      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
		  (unsigned long int) yy_linkstacksize));

      if (yy_linkss + yy_linkstacksize - 1 <= yy_linkssp)
	YYABORT;
    }

  YYDPRINTF ((stderr, "Entering state %d\n", yy_linkstate));

  if (yy_linkstate == YYFINAL)
    YYACCEPT;

  goto yy_linkbackup;

/*-----------.
| yy_linkbackup.  |
`-----------*/
yy_linkbackup:

  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yy_linkn = yy_linkpact[yy_linkstate];
  if (yy_linkn == YYPACT_NINF)
    goto yy_linkdefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid lookahead symbol.  */
  if (yy_linkchar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yy_linkchar = YYLEX;
    }

  if (yy_linkchar <= YYEOF)
    {
      yy_linkchar = yy_linktoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yy_linktoken = YYTRANSLATE (yy_linkchar);
      YY_SYMBOL_PRINT ("Next token is", yy_linktoken, &yy_linklval, &yy_linklloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yy_linkn += yy_linktoken;
  if (yy_linkn < 0 || YYLAST < yy_linkn || yy_linkcheck[yy_linkn] != yy_linktoken)
    goto yy_linkdefault;
  yy_linkn = yy_linktable[yy_linkn];
  if (yy_linkn <= 0)
    {
      if (yy_linkn == 0 || yy_linkn == YYTABLE_NINF)
	goto yy_linkerrlab;
      yy_linkn = -yy_linkn;
      goto yy_linkreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yy_linkerrstatus)
    yy_linkerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yy_linktoken, &yy_linklval, &yy_linklloc);

  /* Discard the shifted token.  */
  yy_linkchar = YYEMPTY;

  yy_linkstate = yy_linkn;
  *++yy_linkvsp = yy_linklval;

  goto yy_linknewstate;


/*-----------------------------------------------------------.
| yy_linkdefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yy_linkdefault:
  yy_linkn = yy_linkdefact[yy_linkstate];
  if (yy_linkn == 0)
    goto yy_linkerrlab;
  goto yy_linkreduce;


/*-----------------------------.
| yy_linkreduce -- Do a reduction.  |
`-----------------------------*/
yy_linkreduce:
  /* yy_linkn is the number of a rule to reduce with.  */
  yy_linklen = yy_linkr2[yy_linkn];

  /* If YYLEN is nonzero, implement the default value of the action:
     `$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yy_linkval = yy_linkvsp[1-yy_linklen];


  YY_REDUCE_PRINT (yy_linkn);
  switch (yy_linkn)
    {
        case 4:

/* Line 1455 of yacc.c  */
#line 56 "link_parser.y"
    {
           and_trees(&inputs, (yy_linkvsp[(3) - (4)].tree));
        }
    break;

  case 5:

/* Line 1455 of yacc.c  */
#line 60 "link_parser.y"
    {
           and_trees(&outputs, (yy_linkvsp[(3) - (4)].tree));
        }
    break;

  case 7:

/* Line 1455 of yacc.c  */
#line 68 "link_parser.y"
    {
            (yy_linkval.tree) = TreeCreate ((yy_linkvsp[(1) - (3)].tree), (yy_linkvsp[(3) - (3)].tree), "&&", AND);
         }
    break;

  case 10:

/* Line 1455 of yacc.c  */
#line 80 "link_parser.y"
    {
	        (yy_linkval.tree) = TreeCreate ((yy_linkvsp[(1) - (3)].tree), (yy_linkvsp[(3) - (3)].tree), ".", DOT);
         }
    break;

  case 11:

/* Line 1455 of yacc.c  */
#line 87 "link_parser.y"
    {
	     (yy_linkval.tree) = TreeCreate (NULL, NULL, (yy_linkvsp[(1) - (1)].string), link_lineno);
	 }
    break;



/* Line 1455 of yacc.c  */
#line 1409 "y.tab.c"
      default: break;
    }
  YY_SYMBOL_PRINT ("-> $$ =", yy_linkr1[yy_linkn], &yy_linkval, &yy_linkloc);

  YYPOPSTACK (yy_linklen);
  yy_linklen = 0;
  YY_STACK_PRINT (yy_linkss, yy_linkssp);

  *++yy_linkvsp = yy_linkval;

  /* Now `shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */

  yy_linkn = yy_linkr1[yy_linkn];

  yy_linkstate = yy_linkpgoto[yy_linkn - YYNTOKENS] + *yy_linkssp;
  if (0 <= yy_linkstate && yy_linkstate <= YYLAST && yy_linkcheck[yy_linkstate] == *yy_linkssp)
    yy_linkstate = yy_linktable[yy_linkstate];
  else
    yy_linkstate = yy_linkdefgoto[yy_linkn - YYNTOKENS];

  goto yy_linknewstate;


/*------------------------------------.
| yy_linkerrlab -- here on detecting error |
`------------------------------------*/
yy_linkerrlab:
  /* If not already recovering from an error, report this error.  */
  if (!yy_linkerrstatus)
    {
      ++yy_linknerrs;
#if ! YYERROR_VERBOSE
      yy_linkerror (YY_("syntax error"));
#else
      {
	YYSIZE_T yy_linksize = yy_linksyntax_error (0, yy_linkstate, yy_linkchar);
	if (yy_linkmsg_alloc < yy_linksize && yy_linkmsg_alloc < YYSTACK_ALLOC_MAXIMUM)
	  {
	    YYSIZE_T yy_linkalloc = 2 * yy_linksize;
	    if (! (yy_linksize <= yy_linkalloc && yy_linkalloc <= YYSTACK_ALLOC_MAXIMUM))
	      yy_linkalloc = YYSTACK_ALLOC_MAXIMUM;
	    if (yy_linkmsg != yy_linkmsgbuf)
	      YYSTACK_FREE (yy_linkmsg);
	    yy_linkmsg = (char *) YYSTACK_ALLOC (yy_linkalloc);
	    if (yy_linkmsg)
	      yy_linkmsg_alloc = yy_linkalloc;
	    else
	      {
		yy_linkmsg = yy_linkmsgbuf;
		yy_linkmsg_alloc = sizeof yy_linkmsgbuf;
	      }
	  }

	if (0 < yy_linksize && yy_linksize <= yy_linkmsg_alloc)
	  {
	    (void) yy_linksyntax_error (yy_linkmsg, yy_linkstate, yy_linkchar);
	    yy_linkerror (yy_linkmsg);
	  }
	else
	  {
	    yy_linkerror (YY_("syntax error"));
	    if (yy_linksize != 0)
	      goto yy_linkexhaustedlab;
	  }
      }
#endif
    }



  if (yy_linkerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
	 error, discard it.  */

      if (yy_linkchar <= YYEOF)
	{
	  /* Return failure if at end of input.  */
	  if (yy_linkchar == YYEOF)
	    YYABORT;
	}
      else
	{
	  yy_linkdestruct ("Error: discarding",
		      yy_linktoken, &yy_linklval);
	  yy_linkchar = YYEMPTY;
	}
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yy_linkerrlab1;


/*---------------------------------------------------.
| yy_linkerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yy_linkerrorlab:

  /* Pacify compilers like GCC when the user code never invokes
     YYERROR and the label yy_linkerrorlab therefore never appears in user
     code.  */
  if (/*CONSTCOND*/ 0)
     goto yy_linkerrorlab;

  /* Do not reclaim the symbols of the rule which action triggered
     this YYERROR.  */
  YYPOPSTACK (yy_linklen);
  yy_linklen = 0;
  YY_STACK_PRINT (yy_linkss, yy_linkssp);
  yy_linkstate = *yy_linkssp;
  goto yy_linkerrlab1;


/*-------------------------------------------------------------.
| yy_linkerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yy_linkerrlab1:
  yy_linkerrstatus = 3;	/* Each real token shifted decrements this.  */

  for (;;)
    {
      yy_linkn = yy_linkpact[yy_linkstate];
      if (yy_linkn != YYPACT_NINF)
	{
	  yy_linkn += YYTERROR;
	  if (0 <= yy_linkn && yy_linkn <= YYLAST && yy_linkcheck[yy_linkn] == YYTERROR)
	    {
	      yy_linkn = yy_linktable[yy_linkn];
	      if (0 < yy_linkn)
		break;
	    }
	}

      /* Pop the current state because it cannot handle the error token.  */
      if (yy_linkssp == yy_linkss)
	YYABORT;


      yy_linkdestruct ("Error: popping",
		  yy_linkstos[yy_linkstate], yy_linkvsp);
      YYPOPSTACK (1);
      yy_linkstate = *yy_linkssp;
      YY_STACK_PRINT (yy_linkss, yy_linkssp);
    }

  *++yy_linkvsp = yy_linklval;


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yy_linkstos[yy_linkn], yy_linkvsp, yy_linklsp);

  yy_linkstate = yy_linkn;
  goto yy_linknewstate;


/*-------------------------------------.
| yy_linkacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yy_linkacceptlab:
  yy_linkresult = 0;
  goto yy_linkreturn;

/*-----------------------------------.
| yy_linkabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yy_linkabortlab:
  yy_linkresult = 1;
  goto yy_linkreturn;

#if !defined(yy_linkoverflow) || YYERROR_VERBOSE
/*-------------------------------------------------.
| yy_linkexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yy_linkexhaustedlab:
  yy_linkerror (YY_("memory exhausted"));
  yy_linkresult = 2;
  /* Fall through.  */
#endif

yy_linkreturn:
  if (yy_linkchar != YYEMPTY)
     yy_linkdestruct ("Cleanup: discarding lookahead",
		 yy_linktoken, &yy_linklval);
  /* Do not reclaim the symbols of the rule which action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yy_linklen);
  YY_STACK_PRINT (yy_linkss, yy_linkssp);
  while (yy_linkssp != yy_linkss)
    {
      yy_linkdestruct ("Cleanup: popping",
		  yy_linkstos[*yy_linkssp], yy_linkvsp);
      YYPOPSTACK (1);
    }
#ifndef yy_linkoverflow
  if (yy_linkss != yy_linkssa)
    YYSTACK_FREE (yy_linkss);
#endif
#if YYERROR_VERBOSE
  if (yy_linkmsg != yy_linkmsgbuf)
    YYSTACK_FREE (yy_linkmsg);
#endif
  /* Make sure YYID is used.  */
  return YYID (yy_linkresult);
}



/* Line 1675 of yacc.c  */
#line 91 "link_parser.y"



/************************************************************************
 * Function:    and_trees                                               *
 *                                                                      *
 * Description:	Links two trees as if specified in an AND expression.	*
 ************************************************************************/

static void and_trees (ptr, tree)
    Tree *ptr;
    Tree  tree;
{
    *ptr = (*ptr == NULL ? tree : TreeCreate (*ptr, tree, "&&", AND));
}


