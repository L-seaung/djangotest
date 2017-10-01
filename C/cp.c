#include "stdio.h"
#include "unistd.h"
#include "fcntl.h"
#include "string.h"

int main(int argc, char * argv[])
{
  int rd_fd, wr_fd;
  char read_buf[128] = {0};
  int rd_ret = 0;
  if(argc < 3)
  {
    printf("please input src file and des file\n");
    return -1;
  }
  
  rd_fd = open(argv[1], O_RDONLY);
  if(rd_fd < 0)
  {
    printf("open src file %s failure \n", argv[1]);
    return -2;
  }
  printf("open src file %s sucess , rd_fd = %d\n", argv[1], rd_fd);
  wr_fd = open(argv[2], O_WRONLY);
  if(wr_fd < 0)
  {
    printf("open file %s failure \n", argv[2] );
    return -3;
  }
  printf("open des file %s sucess wr_fd = %d \n", argv[2], wr_fd);
  
  while(1)
  {
    rd_ret = read(rd_fd, read_buf, 128);
    if(rd_ret < 128)
      break;
    write(wr_fd, read_buf, rd_ret);
    memset(read_buf, 0, 128);
  }
  
  write(wr_fd, read_buf, rd_ret);
  close(rd_fd);
  close(wr_fd);
  return 0;
}
