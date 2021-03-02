nums <- sample(1:100, 20)

for (i in 1:length(nums)){

if (sum(nums[i] > nums) == 0) {
    cat("min is ", nums[i] )
    break
    }
}

