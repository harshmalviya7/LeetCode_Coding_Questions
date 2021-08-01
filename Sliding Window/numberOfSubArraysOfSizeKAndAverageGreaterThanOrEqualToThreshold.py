# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
class Solution {
public:
    int


numOfSubarrays(vector < int > & arr, int
k, int
threshold) {
    int
j = 0;
int
sum = 0;
int
count = 0;

for (int i=0;i < k-1;i++)
{

    sum += arr[i];
}

while (j + k - 1 < arr.size()){
sum=sum+arr[j+k-1];
if (sum / k >= threshold){
count++;
}

sum=sum-arr[j];

j++;

}
return count;

}
};



