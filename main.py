# This is a sample Python script.
import logging
import rankData
import strategy

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
FORMAT = '%(asctime)s : %(filename)s:%(lineno)d -  %(levelname)s :: %(message)s'
logging.basicConfig(filename="kite.log", format=FORMAT, level=logging.INFO)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # Gather data and rank them

    # ranking based on RDX

    # rank = rankData.RankData()
    # df = rank.load_data()
    # rank.rank_data()

    testStrategy = strategy.Strategy()
    testStrategy.load_index()
    testStrategy.evaluate()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
