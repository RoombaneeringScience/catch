if __name__ == '__main__':
    bot = create2api.Create2()
    bot.start()
    bot.safe()
    bot.kinect_power()

    find_ball = FindBall(bot)
    #find_target = FindTarget(bot)
    #controller = Controller(bot)
