from datetime import date, timedelta


def decrease_date(d):
    ans = []
    for i in dates:
        ans.append(i - timedelta(days=1))
    return ans


if __name__ == "__main__":
    t = int(input())
    dates = []
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    for _ in range(t):
        dmy = input().split()
        dates.append(date(int(dmy[2]), months.index(dmy[1])+1, int(dmy[0])))
    ans = decrease_date(dates)
    for i in ans:
        d = i.day
        m = i.month
        y = i.year
        print("%d %s %d"%(d, months[m-1], y))