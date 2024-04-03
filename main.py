from App import App


class CleanData(App):
    index = 'comment'
    input_csv_file_path = 'data.csv'
    output_csv_file_path = 'cleaned_data.csv'


if __name__ == "__main__":
    instance = CleanData()
    instance.main()