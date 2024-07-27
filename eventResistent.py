non_localVisit = 0
justEventLocal = 0
local_resident = 0

def local_event(local_visit):
  global justEventLocal
  totalEventVisit = local_resident + justEventLocal
  return totalEventVisit, local_visit

def local_festival():
  global non_localVisit
  global local_resident
  global justEventLocal
  totalFestivalVisit = non_localVisit + (local_resident - justEventLocal)
  return totalFestivalVisit

local_resident = int(input("지역구민 몇 명이 이벤트에 참여했나요? > "))
non_localVisit = int(input("외지인 몇 명이 축제를 왔나요? > "))
justEventLocal = int(input("이벤트에 참여한 지역구민 중 축제에 참여한 인원은 몇 명인가요? > "))

totalEventVisit, local_visit = local_event(local_resident)
totalFestivalVisit = local_festival()

totalVisit = (totalFestivalVisit-local_resident) + totalEventVisit

print()
print(f"해당 지역에 방문한 인원은 총 {totalVisit}명 입니다.")
print(f"이벤트에 참여한 지역구민은 총 {totalEventVisit}명 입니다.")
print(f"축제에 참여한 인원은 총 {totalFestivalVisit}명 입니다.")