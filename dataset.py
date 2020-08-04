from shutil import copy2
import glob
import os

class DatasetResolver:
    @staticmethod
    def compare_sets_in_folders(path_to_first_folder='', path_to_second_folder='', extension_first='', extension_second=''):
        list_of_first_folder = glob.glob(path_to_first_folder + '/*.' + extension_first)
        list_of_second_folder = glob.glob(path_to_second_folder + '/*.' + extension_second)
        names_objects_in_first_folder = [name.split('/')[-1].split('.')[0] for name in list_of_first_folder]
        names_objects_in_second_folder = [name.split('/')[-1].split('.')[0] for name in list_of_second_folder]
        antiintersection = set(names_objects_in_first_folder) ^ set(names_objects_in_second_folder)
        print(antiintersection)
        # for name in antiintersection:
        #     for name_list in list_of_first_folder:
        #         if name in name_list:
        #             try:
        #                 os.remove(name_list)
        #             except:
        #                 pass
        #
        # for name in antiintersection:
        #     for name_list in list_of_second_folder:
        #         if name in name_list:
        #             try:
        #                 os.remove(name_list)
        #             except:
        #                 pass
    #     new_list_of_first_folder = [os.path.join(path_to_first_folder, name, extension_first) for name in intersection]
    #     new_list_of_second_folder = [os.path.join(path_to_second_folder, name, extension_second) for name in intersection]
    #
    #     # print(len(new_list_of_first_folder), len(new_list_of_second_folder))
    #     return new_list_of_first_folder, new_list_of_second_folder
    #
    # @staticmethod
    # def copy_files_to_folder(src, dst):
    #     copy2(src, dst)


if __name__ == "__main__":
    path_to_first_folder = "/home/evg/Documents/conda/dataset_images/images_to_train_test_val/dataset_leaf_green_blue_red_nir_rededge/train"
    extension_first = 'tif'
    path_to_second_folder = "/home/evg/Documents/conda/dataset_images/images_to_train_test_val/dataset_leaf_green_blue_red_nir_rededge/annot"
    extension_second = 'png'
    class_ = DatasetResolver()
    class_.compare_sets_in_folders(path_to_first_folder, path_to_second_folder, extension_first, extension_second)
