from loader import Loader
from trainer import Training
def main():
    loader = Loader()
    loader.createDataset()
    trainer = Training(loader.train_loader, loader.test_loader, loader.valida_folder)
    trainer.procedure()


if __name__ == "__main__":
    main()