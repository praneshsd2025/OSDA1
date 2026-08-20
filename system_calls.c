#include <stdio.h>
#include <unistd.h>
int main(){
	pid_t pid = getpid();
   	pid_t ppid = getppid();
   	uid_t uid = getuid();

   	printf("Process Information\n");
   	printf("-------------------\n");
   	printf("Process ID (PID)              : %d\n", (int)pid);
   	printf("Parent Process ID (PPID)      : %d\n", (int)ppid);
  	printf("Real User ID (UID)            : %d\n", (int)uid);

   	return 0;
}

