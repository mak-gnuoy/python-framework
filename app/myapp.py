from framework.app import App


class MyApp(App):
    def hello(self):
        self.logger.info("hello, world.")


if __name__ == "__main__":

    def observer(result):
        print(f"Processed: {result}")

    my_app = MyApp(config_path="/app/conf/myapp.toml", callback=observer)
    my_app.hello()
