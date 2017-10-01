#include "stdio.h"
#include "unistd.h"
#include "fcntl.h"

int main(int argc, char * argv[])
{
  int file;
  file = open(argv[1], O_CREAT | O_RDWR, 0777);
  if(file < 0)
  {
    printf("create file %s failure\n", argv[1]);
    return 0;
  }
  
  printf("create file %s sucess!, the file block is :\n", argv[1], file);
  close(file);
  return 0;
}
