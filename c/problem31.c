void print(int* nums, int size)
{
    for(int i = 0; i < size; i++)
    {
        printf("%d", nums[i]);
    }
    printf("\n");
}

void swap(int* nums, int i, int j)
{
    int t = nums[i];
    nums[i] = nums[j];
    nums[j] = t;
    //printf("swap %d %d\n", i, j);
}

void nextPermutation(int* nums, int numsSize) {
    int front = -1;
    for(int i = numsSize - 1; i > 0; --i)
    {
        if(nums[i] > nums[i - 1])
        {
            front = i - 1;
            //printf("front=%d\n", front);
            break;
        }
    }
    //printf("front=%d\n", front);
    int rear = numsSize - 1;
    if(front > -1)
    {
        for(int i = numsSize - 1; i > front; --i)
        {
            if(nums[i] > nums[front])
            {   
                rear = i;
                break;
            }
        }
        swap(nums, front, rear);
    }
    ++front;
    rear = numsSize - 1;
    //printf("front=%d rear=%d\n", front, rear);
    while(front < rear)
    {
        swap(nums, front++, rear--);
    }
}

void test()
{
    int nums[] = { 1, 2, 3 };
    int init[] = { 1, 2, 3 };
    int size = sizeof(nums) / sizeof(int);
    //nextPermutation(nums, size);        
    //print(nums, size);
    //return;
    int i = 0;
    while( i < 6)
    {
        ++i;
        nextPermutation(nums, size);        
        print(nums, size);
    }
}