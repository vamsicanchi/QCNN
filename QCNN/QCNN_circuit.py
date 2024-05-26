import embedding
import logging
import pennylane as qml
import unitary

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# Quantum Circuits for Convolutional layers
def conv_layer1(U, params):
    U(params, wires=[0, 7])
    for i in range(0, 8, 2):
        U(params, wires=[i, i + 1])
    for i in range(1, 7, 2):
        U(params, wires=[i, i + 1])


def conv_layer1_modified(U, params):
    U(params, wires=[0, 7])
    U(params, wires=[2, 3])
    U(params, wires=[4, 5])
    U(params, wires=[6, 7])


def conv_layer2(U, params):
    U(params, wires=[0, 6])
    U(params, wires=[0, 2])
    U(params, wires=[4, 6])
    U(params, wires=[2, 4])


def conv_layer2_modified(U, params):
    U(params, wires=[0, 6])
    U(params, wires=[2, 4])


def conv_layer3(U, params):
    U(params, wires=[0, 4])


def conv_layer3_modified(U, params):
    U(params, wires=[0, 4])


# Quantum Circuits for Pooling layers
def pooling_layer1(V, params):
    for i in range(0, 8, 2):
        V(params, wires=[i + 1, i])


def pooling_layer2(V, params):
    V(params, wires=[2, 0])
    V(params, wires=[6, 4])


def pooling_layer3(V, params):
    V(params, wires=[0, 4])


def pooling_layer1_modified(V, params):
    V(params, wires=[0, 1, 2, 3])


def pooling_layer2_modified(V, params):
    V(params, wires=[0, 2, 4, 6])


# params : are the trainable params for the circuit
def QCNN_structure(U, params, U_params):
    param1 = params[0:U_params]  # 15 params
    param2 = params[U_params : 2 * U_params]  # 15 params
    param3 = params[2 * U_params : 3 * U_params]  # 15 params
    param4 = params[3 * U_params : 3 * U_params + 2]  # 2 params
    param5 = params[3 * U_params + 2 : 3 * U_params + 4]  # 2 params
    param6 = params[3 * U_params + 4 : 3 * U_params + 6]  # 2 params

    # Pooling Ansatz1 is used by default
    conv_layer1(U, param1)
    pooling_layer1(unitary.Pooling_ansatz1, param4)
    conv_layer2(U, param2)
    pooling_layer2(unitary.Pooling_ansatz1, param5)
    conv_layer3(U, param3)
    pooling_layer3(unitary.Pooling_ansatz1, param6)


def QCNN_structure_modified(U, params, U_params):
    param1 = params[0:U_params]
    param2 = params[U_params : 2 * U_params]
    param3 = params[2 * U_params : 3 * U_params]
    param4 = params[3 * U_params : 3 * U_params + 3]
    param5 = params[3 * U_params + 3 : 3 * U_params + 6]

    logger.debug(f"total params -- {params.shape} U_params {U_params}")
    logger.debug(
        f"Params: {param1.shape} {param2.shape} {param3.shape} {param4.shape} {param5.shape}"
    )

    conv_layer1_modified(U, param1)
    pooling_layer1_modified(unitary.Pooling_ansatz_modified, param4)
    conv_layer2_modified(U, param2)
    pooling_layer2_modified(unitary.Pooling_ansatz_modified, param5)
    conv_layer3_modified(U, param3)


def QCNN_structure_without_pooling(U, params, U_params):
    param1 = params[0:U_params]
    param2 = params[U_params : 2 * U_params]
    param3 = params[2 * U_params : 3 * U_params]

    conv_layer1(U, param1)
    conv_layer2(U, param2)
    conv_layer3(U, param3)


def QCNN_1D_circuit(U, params, U_params):
    param1 = params[0:U_params]
    param2 = params[U_params : 2 * U_params]
    param3 = params[2 * U_params : 3 * U_params]

    for i in range(0, 8, 2):
        U(param1, wires=[i, i + 1])
    for i in range(1, 7, 2):
        U(param1, wires=[i, i + 1])

    U(param2, wires=[2, 3])
    U(param2, wires=[4, 5])
    U(param3, wires=[3, 4])


dev = qml.device("default.qubit", wires=8)


@qml.qnode(dev)
def QCNN(X, params, U, U_params, embedding_type="Amplitude", cost_fn="cross_entropy"):

    # Data Embedding
    embedding.data_embedding(X, embedding_type=embedding_type)

    # Quantum Convolutional Neural Network
    if U == "U_TTN":
        QCNN_structure(unitary.U_TTN, params, U_params)
    elif U == "U_5":
        QCNN_structure(unitary.U_5, params, U_params)
    elif U == "U_6":
        QCNN_structure(unitary.U_6, params, U_params)
    elif U == "U_9":
        QCNN_structure(unitary.U_9, params, U_params)
    elif U == "U_13":
        QCNN_structure(unitary.U_13, params, U_params)
    elif U == "U_14":
        QCNN_structure(unitary.U_14, params, U_params)
    elif U == "U_15":
        QCNN_structure(unitary.U_15, params, U_params)
    elif U == "U_SO4":
        QCNN_structure(unitary.U_SO4, params, U_params)
    elif U == "U_SU4":
        QCNN_structure(unitary.U_SU4, params, U_params)
    elif U == "U_SU4_no_pooling":
        QCNN_structure_without_pooling(unitary.U_SU4, params, U_params)
    elif U == "U_SU4_1D":
        QCNN_1D_circuit(unitary.U_SU4, params, U_params)
    elif U == "U_9_1D":
        QCNN_1D_circuit(unitary.U_9, params, U_params)
    elif U == "U_SU4_mod":
        QCNN_structure_modified(unitary.U_SU4, params, U_params)
    else:
        print("Invalid Unitary Ansatze")
        return False

    if cost_fn == "mse":
        result = qml.expval(qml.PauliZ(4))
    elif cost_fn == "cross_entropy":
        if U == "U_SU4_mod":
            result_16_states = qml.probs(wires=[0, 1, 2, 3])
            return result_16_states
        else:
            result = qml.probs(wires=4)
    return result
