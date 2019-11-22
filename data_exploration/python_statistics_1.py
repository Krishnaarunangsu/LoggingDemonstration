import statistics


class StatisticsTest:
    """
    Statistical Test
    """
    example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]

    def __init__(self):
        """
        Initialization
        """

        self.mean = 0
        self.mode = 0
        self.standard_deviation = 0
        self.variance = 0

    def get_mean(self):
        """
        Args
            :param example_list:
        Return:
            mean
        """
        self.mean = statistics.mean(self.example_list)
        return self.mean

    def get_median(self):
        """
        Args
            :param example_list:
        Return:
            mean
        """
        self.median = statistics.mean(self.example_list)
        return self.median

    def get_mode(self):
        """

        :param example_list:
        :return:
        """
        self.mode = statistics.mode(self.example_list)
        return self.mode

    def get_standard_deviation(self):
        """

        :param example_list:
        :return:
        """
        self.standard_deviation = statistics.stdev(self.example_list)
        return self.standard_deviation

    def get_variance(self):
        """

        :param example_list:
        :return:
        """
        self.variance = statistics.variance(self.example_list)
        return self.variance

if __name__ == "__main__":
    statistics_test = StatisticsTest()
    print(f'The Series:{statistics_test.example_list}')
    print(f'Mean:{statistics_test.get_mean()}')
    print(f'Median:{statistics_test.get_median()}')
    print(f'Mode:{statistics_test.get_mode()}')
    print(f'Standard Deviation:{statistics_test.get_standard_deviation()}')
    print(f'Variance:{statistics_test.get_variance()}')
