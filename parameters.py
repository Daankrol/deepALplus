from torchvision import transforms

SEED = 4666


args_pool = {
    "MNIST": {
        "n_epoch": 20,
        "initial_pool": 1000,
        "quota": 40000,
        "batch": 500,
        "name": "MNIST",
        "transform_train": transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
        ),
        "transform": transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
        ),
        "loader_tr_args": {"batch_size": 128, "num_workers": 4},
        "loader_te_args": {"batch_size": 1000, "num_workers": 4},
        "num_class": 10,
        "optimizer": "Adam",
        "pretrained": False,
        "optimizer_args": {"lr": 0.001},
    },
    "MNIST_pretrain": {
        "n_epoch": 20,
        "name": "MNIST",
        "transform_train": transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
        ),
        "transform": transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
        ),
        "loader_tr_args": {"batch_size": 128, "num_workers": 4},
        "loader_te_args": {"batch_size": 1000, "num_workers": 4},
        "num_class": 10,
        "optimizer": "Adam",
        "pretrained": True,
        "optimizer_args": {"lr": 0.001},
    },
    "FashionMNIST": {
        "n_epoch": 20,
        "name": "FashionMNIST",
        "transform_train": transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.286,), (0.3529,))]
        ),
        "transform": transforms.Compose(
            [transforms.ToTensor(), transforms.Normalize((0.286,), (0.3529,))]
        ),
        "loader_tr_args": {"batch_size": 128, "num_workers": 4},
        "loader_te_args": {"batch_size": 1000, "num_workers": 4},
        "optimizer": "Adam",
        "num_class": 10,
        "pretrained": False,
        "optimizer_args": {"lr": 0.001},
    },
    "EMNIST": {
        "n_epoch": 20,
        "name": "EMNIST",
        "transform_train": transforms.Compose([transforms.ToTensor()]),
        "transform": transforms.Compose([transforms.ToTensor()]),
        "loader_tr_args": {"batch_size": 128, "num_workers": 4},
        "loader_te_args": {"batch_size": 1000, "num_workers": 4},
        "optimizer": "Adam",
        "num_class": 62,
        "pretrained": False,
        "optimizer_args": {"lr": 0.001},
    },
    "SVHN": {
        "n_epoch": 20,
        "name": "SVHN",
        "transform_train": transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Normalize(
                    (0.4377, 0.4438, 0.4728), (0.1980, 0.2010, 0.1970)
                ),
            ]
        ),
        "transform": transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Normalize(
                    (0.4377, 0.4438, 0.4728), (0.1980, 0.2010, 0.1970)
                ),
            ]
        ),
        "loader_tr_args": {"batch_size": 128, "num_workers": 4},
        "loader_te_args": {"batch_size": 1000, "num_workers": 4},
        "optimizer": "Adam",
        "num_class": 10,
        "pretrained": False,
        "optimizer_args": {"lr": 0.001},
    },
    "CIFAR10": {
        "n_epoch": 30,
        "name": "CIFAR10",
        "transform_train": transforms.Compose(
            [
                transforms.RandomCrop(size=32, padding=4),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),
                transforms.Normalize(
                    (0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616)
                ),
            ]
        ),
        "transform": transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Normalize(
                    (0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616)
                ),
            ]
        ),
        "loader_tr_args": {"batch_size": 128, "num_workers": 4},
        "loader_te_args": {"batch_size": 1000, "num_workers": 4},
        "num_class": 10,
        "pretrained": False,
        "optimizer": "Adam",
        "optimizer_args": {"lr": 0.001},
    },
    "CIFAR10_imb": {
        "n_epoch": 30,
        "name": "CIFAR10_imb",
        "transform_train": transforms.Compose(
            [
                transforms.RandomCrop(size=32, padding=4),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),
                transforms.Normalize(
                    (0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616)
                ),
            ]
        ),
        "transform": transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Normalize(
                    (0.4914, 0.4822, 0.4465), (0.2470, 0.2435, 0.2616)
                ),
            ]
        ),
        "loader_tr_args": {"batch_size": 128, "num_workers": 4},
        "loader_te_args": {"batch_size": 1000, "num_workers": 4},
        "num_class": 10,
        "optimizer": "Adam",
        "pretrained": False,
        "optimizer_args": {"lr": 0.001},
    },
    "CIFAR100": {
        "n_epoch": 40,
        "initial_pool": 1000,
        "quota": 40000,
        "batch": 500,
        "name": "CIFAR100",
        "transform_train": transforms.Compose(
            [
                transforms.RandomCrop(size=32, padding=4),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),
                transforms.Normalize(
                    (0.5071, 0.4865, 0.4409), (0.2673, 0.2564, 0.2762)
                ),
            ]
        ),
        "transform": transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Normalize(
                    (0.5071, 0.4865, 0.4409), (0.2673, 0.2564, 0.2762)
                ),
            ]
        ),
        "loader_tr_args": {"batch_size": 128, "num_workers": 4},
        "loader_te_args": {"batch_size": 1000, "num_workers": 4},
        "num_class": 100,
        "optimizer": "Adam",
        "pretrained": False,
        "optimizer_args": {"lr": 0.001},
    },
    "TinyImageNet": {
        "n_epoch": 40,
        "name": "TinyImageNet",
        "transform_train": transforms.Compose(
            [
                transforms.RandomRotation(20),
                transforms.RandomHorizontalFlip(0.5),
                transforms.ToTensor(),
                transforms.Normalize(
                    [0.4802, 0.4481, 0.3975], [0.2302, 0.2265, 0.2262]
                ),
            ]
        ),
        "transform": transforms.Compose(
            [
                transforms.ToTensor(),
                transforms.Normalize(
                    [0.4802, 0.4481, 0.3975], [0.2302, 0.2265, 0.2262]
                ),
            ]
        ),
        "loader_tr_args": {"batch_size": 128, "num_workers": 4},
        "loader_te_args": {"batch_size": 1000, "num_workers": 4},
        "num_class": 200,
        "optimizer": "Adam",
        "pretrained": False,
        "optimizer_args": {"lr": 0.001},
    },
    "openml": {
        "n_epoch": 5,
        "name": "openml",
        "transform_train": transforms.Compose([transforms.ToTensor()]),
        "transform": transforms.Compose([transforms.ToTensor()]),
        "loader_tr_args": {"batch_size": 128, "num_workers": 2},
        "loader_te_args": {"batch_size": 1000, "num_workers": 2},
        "num_class": 26,
        "optimizer": "Adam",
        "pretrained": False,
        "optimizer_args": {"lr": 0.01},
    },
    "PneumoniaMNIST": {
        "n_epoch": 10,
        "name": "PneumoniaMNIST",
        "transform_train": transforms.Compose(
            [
                transforms.Resize(255),
                transforms.CenterCrop(224),
                transforms.RandomHorizontalFlip(),
                transforms.RandomRotation(10),
                transforms.RandomGrayscale(),
                transforms.RandomAffine(translate=(0.05, 0.05), degrees=0),
                transforms.ToTensor(),
            ]
        ),
        "transform": transforms.Compose(
            [transforms.Resize(255), transforms.CenterCrop(224), transforms.ToTensor()]
        ),
        "loader_tr_args": {"batch_size": 32, "num_workers": 2},
        "loader_te_args": {"batch_size": 128, "num_workers": 2},
        "num_class": 2,
        "optimizer": "SGD",
        "pretrained": False,
        "optimizer_args": {"lr": 0.001},
    },
    "waterbirds": {
        "n_epoch": 30,
        "name": "waterbirds",
        "transform_train": transforms.Compose(
            [transforms.RandomHorizontalFlip(), transforms.ToTensor()]
        ),
        # transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])]),
        "transform": transforms.Compose([transforms.ToTensor()]),
        # transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])]),
        "loader_tr_args": {"batch_size": 32, "num_workers": 2},
        "loader_te_args": {"batch_size": 128, "num_workers": 2},
        "optimizer": "SGD",
        "num_class": 2,
        "pretrained": False,
        "optimizer_args": {"lr": 0.0001, "weight_decay": 1e-5, "momentum": 0.9},
    },
    "waterbirds_pretrain": {
        "n_epoch": 30,
        "name": "waterbirds_pretrain",
        "transform_train": transforms.Compose(
            [transforms.RandomHorizontalFlip(), transforms.ToTensor()]
        ),
        # transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])]),
        "transform": transforms.Compose([transforms.ToTensor()]),
        # transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])]),
        "loader_tr_args": {"batch_size": 32, "num_workers": 2},
        "loader_te_args": {"batch_size": 128, "num_workers": 2},
        "optimizer": "SGD",
        "pretrained": True,
        "num_class": 2,
        "optimizer_args": {"lr": 0.0005, "weight_decay": 1e-5, "momentum": 0.9},
    },
    "BreakHis": {
        "n_epoch": 10,
        "name": "BreakHis",
        "transform_train": transforms.Compose(
            [
                transforms.RandomRotation(90),
                transforms.RandomHorizontalFlip(0.8),
                transforms.RandomResizedCrop(224),
                transforms.ColorJitter(
                    brightness=0.4, contrast=0.4, saturation=0.4, hue=0.1
                ),
                transforms.ToTensor(),
                transforms.Normalize(
                    (0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)
                ),
            ]
        ),
        "transform": transforms.Compose(
            [
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize(
                    (0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)
                ),
            ]
        ),
        "loader_tr_args": {"batch_size": 32, "num_workers": 2},
        "loader_te_args": {"batch_size": 128, "num_workers": 2},
        "optimizer": "SGD",
        "num_class": 2,
        "pretrained": False,
        "optimizer_args": {"lr": 0.001},
    },
}
