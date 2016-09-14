#include "stdio.h"
#include "unistd.h"
#include "fcntl.h"


int main(int argc, char * argv[])
{
  int file;
  int write_file;
  char *buffer[] = "hello linux, your are beautiful!";
  int buffer_size = 128;
  
  file = open(argv[1], O_RDWR);
  if(file < 0)
  {
    printf("open %s file failure\n", argv[1]);
    return -1;
  }
  printf("open %s file sucess\n", argv[1]);
  write_file = write(file, buffer, buffer_size);
  printf("write %s file sucess!\n", argv[2]);
  close(file);
  return 0;
}
