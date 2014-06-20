# Topological Sort
# Vertex Definiton
class Course:
    def __init__(self, name, id, prerequisites = None):
        self.name = name
        self.id = id
        self.prerequisites = prerequisites

# Edges
class Prequisite:
    def __init__(self, course_id, next = None):
        self.course_id = course_id
        self.next = next

class CoursePlanner:
    output = []
    def __init__(self, courses):
        self.courses = courses

    def courseCount(self):
        return len(self.courses)

    def arrangeCourses(self):
        visited = set()
        for course_id in courses.keys():
            if course_id not in visited:
                self.__dfs(course_id, visited)

        return self.output[::-1]

    def __dfs(self, course_id, visited):
        visited.add(course_id)

        current_prerequisite = self.courses[course_id].prerequisites
        while current_prerequisite:
            if current_prerequisite.course_id not in visited:
                self.__dfs(current_prerequisite.course_id, visited)
            current_prerequisite = current_prerequisite.next

        self.output.append(self.courses[course_id].name)


# Main program
cs_101 = Course("CS101", 101)
cs_102 = Course("CS102", 102)
cs_250 = Course("CS250", 250)
cs_301 = Course("CS301", 301)
cs_450 = Course("CS450", 450)
cs_469 = Course("CS469", 469)
cs_501 = Course("CS501", 501)

p1_102 = Prequisite(cs_101.id)
p2_250 = Prequisite(cs_101.id, Prequisite(cs_102.id))
p3_301 = Prequisite(cs_102.id)
p4_450 = Prequisite(cs_250.id)
p5_469 = Prequisite(cs_250.id, Prequisite(cs_301.id, Prequisite(cs_450.id)))
p6_501 = Prequisite(cs_301.id)

cs_101.prerequisites = None
cs_102.prerequisites = p1_102
cs_250.prerequisites = p2_250
cs_301.prerequisites = p3_301
cs_450.prerequisites = p4_450
cs_469.prerequisites = p5_469
cs_501.prerequisites = p6_501

courses = {
    cs_101.id:cs_101,
    cs_102.id:cs_102,
    cs_250.id:cs_250,
    cs_301.id:cs_301,
    cs_450.id:cs_450,
    cs_469.id:cs_469,
    cs_501.id:cs_501}

planner = CoursePlanner(courses)
print("Course count: %d" %planner.courseCount())
print(planner.arrangeCourses())
