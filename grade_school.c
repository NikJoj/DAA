#include<stdio.h>

int main(){

    int a[5000],b[5000],r[15];
    int t,p=0,i,j,m,n,step=0;

    // printf("Enter size n: ");
    // scanf("%d",&m);
    // scanf("%d",&n);
    
    // printf("Enter first number: ");
    // for(i=(n-1);i>=0;i--)
    //     scanf("%d",&a[i]);
     
    // printf("Enter second number: ");
    // for(i=(n-1);i>=0;i--)
    //     scanf("%d",&b[i]);
    
    // for(i=0;i<n;i++)
    //     printf("%d",a[i]);
    // printf("\n");
    
    // for(i=0;i<n;i++)
    //     printf("%d",b[i]);
    // printf("\n");

    // for(i=n;i<5000;i++)
    //     a[i]=0;

    // for(i=n;i<5000;i++)
    //     b[i]=0;

    // for(i=0;i<15;i++)
    //     r[i]=0;

    // for(i=0;i<m;i++){
    //     p=i;
    //     for(j=0;j<n;j++){
    //         t=b[i]*a[j];
           // if(t/10)
            

    //         if((r[p]+(t%10))/10){
    //             t=(r[p]+(t%10));
    //             r[p]=(t%10);
    //         }
    //         else
    //             r[p]=(t%10)+r[p];
    //         p++;
    //         r[p]=(t/10)+r[p];
    //     }

    //     for(int k=0;k<15;k++)
    //     printf("%d",r[k]);
    // }

    int k=1;

    while(k<5000){
        step = 0;
        for(i=0;i<k;i++){
            for(j=0;j<k;j++){
                // t=a[j]*b[i];
                // r[i+j]+=t;
                // r[i+j+1]+=r[i+j]/10;
                // r[i+j]%=10;

                step++;
            }
        }

        printf("Number of steps for length %d is %d \n",k,step);
        k = k*2;

    }

    
    // int pos;

    // for(i=14;i>0;i--)
    //     if(r[i]!=0){
    //         pos=i;
    //         break;
    //     }

    // for(i=pos;i>=0;i--)
    //     printf("%d",r[i]);
    // printf(" is the result. \nSteps: %d \n",step);


}