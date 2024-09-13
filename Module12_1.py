import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    # Тест метода walk
    def test_walk(self):
        runner = Runner("Test1")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    # Тест метода run
    def test_run(self):
        runner = Runner("Test2")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    # Тест методов run и walk
    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
