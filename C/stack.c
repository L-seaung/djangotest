#include<stdio.h>
#include<malloc.h>
#include<stdlib.h>

typedef struct Node
{
  int data;
  struct Node *pNext;
}NODE, *PNODE;

typedef struct stack
{
  PNODE pTop;
  PNODE pBottom;
}STACK, * PSTACK;

void initstack(PSTACK);

int main(void)
{
  STACK S;
  int values;
}

void initstack(PSTACK ps)
{
  ps->pTop = (PNODE)malloc(sizeof(NODE));
  if(NULL == ps->pTop)
  {
    printf("storge malloc fail.....");
    exit(-1);
  }
  else{
    ps->pBottom = ps->pTop;
    ps->pTop->pNext = NULL;
  }
}
