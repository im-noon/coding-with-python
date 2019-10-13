
def hanoi(n,left_pole, middle_pole, right_pole):

    # when n-1 disks are in the final position
    if n == 1:
        move_disk(left_pole, right_pole)
        return
    # moving n-1 disks of the largest one to be able to move
    hanoi(n-1, left_pole, right_pole, middle_pole)
    move_disk(left_pole, right_pole)
    # placing n-1 disks on the top of the largest one
    hanoi(n - 1, middle_pole, left_pole, right_pole)

def move_disk(fp,tp):
    print("moving disk from",fp,"to",tp)


if __name__ == "__main__":
    hanoi(3, "A", "B", "C")