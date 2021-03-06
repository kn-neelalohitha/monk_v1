from pytorch.models.imports import *
from system.imports import *


@accepts(dict, int, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=True)
def get_layer(network_layer, num_ftrs):
    layer_name = network_layer["name"];
    layer_params = network_layer["params"];
    
    if(layer_name == "linear"):
        layer = nn.Linear(num_ftrs, layer_params["out_features"])
        num_ftrs = layer_params["out_features"];
    elif(layer_name == "dropout"):
        layer = nn.Dropout(p=layer_params["p"]);
    elif(layer_name == "elu"):
        layer = nn.ELU(alpha=layer_params["alpha"]);
    elif(layer_name == "hardshrink"):
        layer = nn.Hardshrink(lambd=layer_params["lambd"]);
    elif(layer_name == "hardtanh"):
        layer = nn.Hardtanh(min_val=layer_params["min_val"], max_val=layer_params["max_val"]);
    elif(layer_name == "leakyrelu"):
        layer = nn.LeakyReLU(negative_slope=layer_params["negative_slope"]);
    elif(layer_name == "logsigmoid"):
        layer = nn.LogSigmoid();
    elif(layer_name == "prelu"):
        layer = nn.PReLU(num_parameters=layer_params["num_parameters"], init=layer_params["init"]);
    elif(layer_name == "relu"):
        layer = nn.ReLU();
    elif(layer_name == "relu6"):
        layer = nn.ReLU6();
    elif(layer_name == "rrelu"):
        layer = nn.RReLU(lower=layer_params["lower"], upper=layer_params["upper"]);
    elif(layer_name == "selu"):
        layer = nn.SELU();
    elif(layer_name == "celu"):
        layer = nn.CELU(alpha=layer_params["alpha"]);
    elif(layer_name == "sigmoid"):
        layer = nn.Sigmoid();
    elif(layer_name == "softplus"):
        layer = nn.Softplus(beta=layer_params["beta"], threshold=layer_params["threshold"]);
    elif(layer_name == "softshrink"):
        layer = nn.Softshrink(lambd=layer_params["lambd"]);
    elif(layer_name == "softsign"):
        layer = nn.Softsign();
    elif(layer_name == "tanh"):
        layer = nn.Tanh();
    elif(layer_name == "tanhshrink"):
        layer = nn.Tanhshrink();
    elif(layer_name == "threshold"):
        layer = nn.Threshold(threshold=layer_params["threshold"], value=layer_params["value"]);
    elif(layer_name == "softmin"):
        layer = nn.Softmin();
    elif(layer_name == "softmax"):
        layer = nn.Softmax();
    elif(layer_name == "logsoftmax"):
        layer = nn.LogSoftmax();

    return layer, num_ftrs;






@accepts(dict, num_neurons=int, final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def layer_linear(system_dict, num_neurons=512, final_layer=False):
    tmp = {};
    tmp["name"] = "linear";
    tmp["params"] = {};
    tmp["params"]["out_features"] = num_neurons;
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;


@accepts(dict, probability=float, final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def layer_dropout(system_dict, probability=0.5, final_layer=False):
    tmp = {};
    tmp["name"] = "dropout";
    tmp["params"] = {};
    tmp["params"]["p"] = probability;
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;



@accepts(dict, alpha=[int, float], final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_elu(system_dict, alpha=1.0, final_layer=False):
    tmp = {};
    tmp["name"] = "elu";
    tmp["params"] = {};
    tmp["params"]["alpha"] = alpha;
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;



@accepts(dict, lambd=[int, float], final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_hardshrink(system_dict, lambd=0.5, final_layer=False):
    tmp = {};
    tmp["name"] = "hardshrink";
    tmp["params"] = {};
    tmp["params"]["lambd"] = lambd;
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;


@accepts(dict, min_val=[int, float], max_val=[int, float], final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_hardtanh(system_dict, min_val=-1.0, max_val=1.0, final_layer=False):
    tmp = {};
    tmp["name"] = "hardtanh";
    tmp["params"] = {};
    tmp["params"]["min_val"] = min_val;
    tmp["params"]["max_val"] = max_val;
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;


@accepts(dict, negative_slope=[int, float], final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_leakyrelu(system_dict, negative_slope=0.01, final_layer=False):
    tmp = {};
    tmp["name"] = "leakyrelu";
    tmp["params"] = {};
    tmp["params"]["negative_slope"] = negative_slope; 
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;



@accepts(dict, final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_logsigmoid(system_dict, final_layer=False):
    tmp = {};
    tmp["name"] = "logsigmoid";
    tmp["params"] = {};
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;




@accepts(dict, num_parameters=int, init=[int, float], final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_prelu(system_dict, num_parameters=1, init=0.25, final_layer=False):
    tmp = {};
    tmp["name"] = "prelu";
    tmp["params"] = {};
    tmp["params"]["num_parameters"] = num_parameters; 
    tmp["params"]["init"] = init; 
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;



@accepts(dict, final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_relu(system_dict, final_layer=False):
    tmp = {};
    tmp["name"] = "relu";
    tmp["params"] = {};
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;



@accepts(dict, final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_relu6(system_dict, final_layer=False):
    tmp = {};
    tmp["name"] = "relu6";
    tmp["params"] = {};
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;



@accepts(dict, lower=[int, float], upper=[int, float], final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_rrelu(system_dict, lower=0.125, upper=0.333, final_layer=False):
    tmp = {};
    tmp["name"] = "rrelu";
    tmp["params"] = {};
    tmp["params"]["lower"] = lower; 
    tmp["params"]["upper"] = upper; 
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;



@accepts(dict, final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_selu(system_dict, final_layer=False):
    tmp = {};
    tmp["name"] = "selu";
    tmp["params"] = {};
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;


@accepts(dict, alpha=[int, float], final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_celu(system_dict, alpha=1.0, final_layer=False):
    tmp = {};
    tmp["name"] = "celu";
    tmp["params"] = {};
    tmp["params"]["alpha"] = alpha;
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;




@accepts(dict, final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_sigmoid(system_dict, final_layer=False):
    tmp = {};
    tmp["name"] = "sigmoid";
    tmp["params"] = {};
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;



@accepts(dict, beta=[int, float], threshold=[int, float], final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_softplus(system_dict, beta=1, threshold=20, final_layer=False):
    tmp = {};
    tmp["name"] = "softplus";
    tmp["params"] = {};
    tmp["params"]["beta"] = beta; 
    tmp["params"]["threshold"] = threshold; 
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;




@accepts(dict, lambd=[int, float], final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_softshrink(system_dict, lambd=0.5, final_layer=False):
    tmp = {};
    tmp["name"] = "softshrink";
    tmp["params"] = {};
    tmp["params"]["lambd"] = lambd;
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;



@accepts(dict, final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_softsign(system_dict, final_layer=False):
    tmp = {};
    tmp["name"] = "softsign";
    tmp["params"] = {};
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;



@accepts(dict, final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_tanh(system_dict, final_layer=False):
    tmp = {};
    tmp["name"] = "tanh";
    tmp["params"] = {};
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;



@accepts(dict, final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_tanhshrink(system_dict, final_layer=False):
    tmp = {};
    tmp["name"] = "tanhshrink";
    tmp["params"] = {};
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;



@accepts(dict, [int, float], [int, float], final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_threshold(system_dict, threshold, value, final_layer=False):
    tmp = {};
    tmp["name"] = "threshold";
    tmp["params"] = {};
    tmp["params"]["value"] = value; 
    tmp["params"]["threshold"] = threshold;
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;




@accepts(dict, final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_softmin(system_dict, final_layer=False):
    tmp = {};
    tmp["name"] = "softmin";
    tmp["params"] = {};
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;



@accepts(dict, final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_softmax(system_dict, final_layer=False):
    tmp = {};
    tmp["name"] = "softmax";
    tmp["params"] = {};
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;



@accepts(dict, final_layer=bool, post_trace=True)
@TraceFunction(trace_args=False, trace_rv=False)
def activation_logsoftmax(system_dict, final_layer=False):
    tmp = {};
    tmp["name"] = "logsoftmax";
    tmp["params"] = {};
    system_dict["model"]["custom_network"].append(tmp);
    system_dict["model"]["final_layer"] = final_layer;

    return system_dict;



@accepts(dict, [int, tuple], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=True)
def custom_model_get_layer(network_layer, current_in_shape):
    layer_name = network_layer["name"];
    layer_params = network_layer["params"];

    if(layer_name == "convolution1d"):
        layer, current_in_shape = custom_model_layer_convolution1d(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "convolution2d"):
        layer, current_in_shape = custom_model_layer_convolution2d(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "convolution3d"):
        layer, current_in_shape = custom_model_layer_convolution3d(layer_params, current_in_shape);
        return layer, current_in_shape;

    elif(layer_name == "transposed_convolution1d"):
        layer, current_in_shape = custom_model_layer_transposed_convolution1d(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "transposed_convolution2d"):
        layer, current_in_shape = custom_model_layer_transposed_convolution2d(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "transposed_convolution3d"):
        layer, current_in_shape = custom_model_layer_transposed_convolution3d(layer_params, current_in_shape);
        return layer, current_in_shape;


    elif(layer_name == "max_pooling1d"):
        layer, current_in_shape = custom_model_layer_max_pooling1d(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "max_pooling2d"):
        layer, current_in_shape = custom_model_layer_max_pooling2d(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "max_pooling3d"):
        layer, current_in_shape = custom_model_layer_max_pooling3d(layer_params, current_in_shape);
        return layer, current_in_shape;


    elif(layer_name == "average_pooling1d"):
        layer, current_in_shape = custom_model_layer_average_pooling1d(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "average_pooling2d"):
        layer, current_in_shape = custom_model_layer_average_pooling2d(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "average_pooling3d"):
        layer, current_in_shape = custom_model_layer_average_pooling3d(layer_params, current_in_shape);
        return layer, current_in_shape;


    elif(layer_name == "global_max_pooling1d"):
        layer, current_in_shape = custom_model_layer_global_max_pooling1d(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "global_max_pooling2d"):
        layer, current_in_shape = custom_model_layer_global_max_pooling2d(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "global_max_pooling3d"):
        layer, current_in_shape = custom_model_layer_global_max_pooling3d(layer_params, current_in_shape);
        return layer, current_in_shape;


    elif(layer_name == "global_average_pooling1d"):
        layer, current_in_shape = custom_model_layer_global_average_pooling1d(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "global_average_pooling2d"):
        layer, current_in_shape = custom_model_layer_global_average_pooling2d(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "global_average_pooling3d"):
        layer, current_in_shape = custom_model_layer_global_average_pooling3d(layer_params, current_in_shape);
        return layer, current_in_shape;


    elif(layer_name == "fully_connected"):
        layer, current_in_shape = custom_model_layer_fully_connected(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "flatten"):
        layer, current_in_shape = custom_model_layer_flatten(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "dropout"):
        layer, current_in_shape = custom_model_layer_dropout(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "identity"):
        layer, current_in_shape = custom_model_layer_identity(layer_params, current_in_shape);
        return layer, current_in_shape;


    elif(layer_name == "batch_normalization"):
        layer, current_in_shape = custom_model_layer_batch_normalization(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "instance_normalization"):
        layer, current_in_shape = custom_model_layer_instance_normalization(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "layer_normalization"):
        layer, current_in_shape = custom_model_layer_layer_normalization(layer_params, current_in_shape);
        return layer, current_in_shape;


    elif(layer_name == "relu"):
        layer, current_in_shape = custom_model_activation_relu(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "sigmoid"):
        layer, current_in_shape = custom_model_activation_sigmoid(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "tanh"):
        layer, current_in_shape = custom_model_activation_tanh(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "softplus"):
        layer, current_in_shape = custom_model_activation_softplus(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "softsign"):
        layer, current_in_shape = custom_model_activation_softsign(layer_params, current_in_shape);
        return layer, current_in_shape;

    elif(layer_name == "elu"):
        layer, current_in_shape = custom_model_activation_elu(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "leaky_relu"):
        layer, current_in_shape = custom_model_activation_leaky_relu(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "prelu"):
        layer, current_in_shape = custom_model_activation_prelu(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "selu"):
        layer, current_in_shape = custom_model_activation_selu(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "hardshrink"):
        layer, current_in_shape = custom_model_activation_hardshrink(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "hardtanh"):
        layer, current_in_shape = custom_model_activation_hardtanh(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "logsigmoid"):
        layer, current_in_shape = custom_model_activation_logsigmoid(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "relu6"):
        layer, current_in_shape = custom_model_activation_relu6(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "rrelu"):
        layer, current_in_shape = custom_model_activation_rrelu(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "celu"):
        layer, current_in_shape = custom_model_activation_celu(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "softshrink"):
        layer, current_in_shape = custom_model_activation_softshrink(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "tanhshrink"):
        layer, current_in_shape = custom_model_activation_tanhshrink(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "threshold"):
        layer, current_in_shape = custom_model_activation_threshold(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "softmin"):
        layer, current_in_shape = custom_model_activation_softmin(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "softmax"):
        layer, current_in_shape = custom_model_activation_softmax(layer_params, current_in_shape);
        return layer, current_in_shape;
    elif(layer_name == "logsoftmax"):
        layer, current_in_shape = custom_model_activation_logsoftmax(layer_params, current_in_shape);
        return layer, current_in_shape;





@accepts(dict, tuple, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_convolution1d(params, current_in_shape):
    if(params["padding"] == "in_eq_out" and params["stride"]==1):
        params["padding"] = (params["dilation"]*(params["kernel_size"] - 1) - params["stride"] + 1)//2;
    elif(params["padding"] == "in_eq_out" and params["stride"]!=1):
        params["padding"] = 0;

    in_channels = current_in_shape[0];

    layer = nn.Conv1d(in_channels,
                        params["output_channels"], 
                        params["kernel_size"], 
                        stride=params["stride"], 
                        padding=params["padding"], 
                        dilation=params["dilation"], 
                        groups=params["groups"], 
                        bias=params["use_bias"]);

    c, w = current_in_shape
    x = torch.randn(1, c, w);
    y = layer(x)
    current_in_shape = (y.shape[1], y.shape[2])
    
    return layer, current_in_shape


@accepts(dict, tuple, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_convolution2d(params, current_in_shape):
    if(params["padding"] == "in_eq_out" and params["stride"]==1):
        params["padding"] = (params["dilation"]*(params["kernel_size"] - 1) - params["stride"] + 1)//2;
    elif(params["padding"] == "in_eq_out" and params["stride"]!=1):
        params["padding"] = 0;

    in_channels = current_in_shape[0];

    layer = nn.Conv2d(in_channels,
                        params["output_channels"], 
                        params["kernel_size"], 
                        stride=params["stride"], 
                        padding=params["padding"], 
                        dilation=params["dilation"], 
                        groups=params["groups"], 
                        bias=params["use_bias"]);

    c, h, w = current_in_shape
    x = torch.randn(1, c, h, w);
    y = layer(x)
    current_in_shape = (y.shape[1], y.shape[2], y.shape[3])

    return layer, current_in_shape



@accepts(dict, tuple, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_convolution3d(params, current_in_shape):
    if(params["padding"] == "in_eq_out" and params["stride"]==1):
        params["padding"] = (params["dilation"]*(params["kernel_size"] - 1) - params["stride"] + 1)//2;
    elif(params["padding"] == "in_eq_out" and params["stride"]!=1):
        params["padding"] = 0;

    in_channels = current_in_shape[0];
        
    layer = nn.Conv3d(in_channels,
                        params["output_channels"], 
                        params["kernel_size"], 
                        stride=params["stride"], 
                        padding=params["padding"], 
                        dilation=params["dilation"], 
                        groups=params["groups"], 
                        bias=params["use_bias"]);

    c, d, h, w = current_in_shape
    x = torch.randn(1, c, d, h, w);
    y = layer(x)
    current_in_shape = (y.shape[1], y.shape[2], y.shape[3], y.shape[4])
    
    return layer, current_in_shape



@accepts(dict, tuple, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_transposed_convolution1d(params, current_in_shape):
    if(params["padding"] == "in_eq_out" and params["stride"]==1):
        params["padding"] = (params["kernel_size"] + params["output_padding"])//2;
    elif(params["padding"] == "in_eq_out" and params["stride"]!=1):
        params["padding"] = 0;

    in_channels = current_in_shape[0];

    layer = nn.ConvTranspose1d(in_channels,
                                params["output_channels"], 
                                params["kernel_size"], 
                                stride=params["stride"], 
                                padding=params["padding"], 
                                dilation=params["dilation"], 
                                groups=params["groups"],
                                output_padding=params["output_padding"], 
                                bias=params["use_bias"])

    c, w = current_in_shape
    x = torch.randn(1, c, w);
    y = layer(x)
    current_in_shape = (y.shape[1], y.shape[2])

    return layer, current_in_shape


@accepts(dict, tuple, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_transposed_convolution2d(params, current_in_shape):
    if(params["padding"] == "in_eq_out" and params["stride"]==1):
        params["padding"] = (params["kernel_size"] + params["output_padding"])//2;
    elif(params["padding"] == "in_eq_out" and params["stride"]!=1):
        params["padding"] = 0;

    in_channels = current_in_shape[0];

    layer = nn.ConvTranspose2d(in_channels,
                                params["output_channels"], 
                                params["kernel_size"], 
                                stride=params["stride"], 
                                padding=params["padding"], 
                                dilation=params["dilation"], 
                                groups=params["groups"],
                                output_padding=params["output_padding"], 
                                bias=params["use_bias"])

    c, h, w = current_in_shape
    x = torch.randn(1, c, h, w);
    y = layer(x)
    current_in_shape = (y.shape[1], y.shape[2], y.shape[3])

    return layer, current_in_shape



@accepts(dict, tuple, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_transposed_convolution3d(params, current_in_shape):
    if(params["padding"] == "in_eq_out" and params["stride"]==1):
        params["padding"] = (params["kernel_size"] + params["output_padding"])//2;
    elif(params["padding"] == "in_eq_out" and params["stride"]!=1):
        params["padding"] = 0;

    in_channels = current_in_shape[0];

    layer = nn.ConvTranspose3d(in_channels,
                                params["output_channels"], 
                                params["kernel_size"], 
                                stride=params["stride"], 
                                padding=params["padding"], 
                                dilation=params["dilation"], 
                                groups=params["groups"],
                                output_padding=params["output_padding"], 
                                bias=params["use_bias"])

    c, d, h, w = current_in_shape
    x = torch.randn(1, c, d, h, w);
    y = layer(x)
    current_in_shape = (y.shape[1], y.shape[2], y.shape[3], y.shape[4])

    return layer, current_in_shape



@accepts(dict, tuple, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_max_pooling1d(params, current_in_shape):

    in_channels = current_in_shape[0];

    layer = nn.MaxPool1d(params["kernel_size"], 
                        stride=params["stride"], 
                        padding=params["padding"],
                        ceil_mode=params["ceil_mode"],
                        return_indices=params["return_indices"]);
    
    c, w = current_in_shape
    x = torch.randn(1, c, w);
    y = layer(x)
    current_in_shape = (y.shape[1], y.shape[2])

    return layer, current_in_shape


@accepts(dict, tuple, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_max_pooling2d(params, current_in_shape):

    in_channels = current_in_shape[0];

    layer = nn.MaxPool2d(params["kernel_size"], 
                        stride=params["stride"], 
                        padding=params["padding"],
                        ceil_mode=params["ceil_mode"],
                        return_indices=params["return_indices"]);
    
    c, h, w = current_in_shape
    x = torch.randn(1, c, h, w);
    y = layer(x)
    current_in_shape = (y.shape[1], y.shape[2], y.shape[3])

    return layer, current_in_shape


@accepts(dict, tuple, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_max_pooling3d(params, current_in_shape):

    in_channels = current_in_shape[0];

    layer = nn.MaxPool3d(params["kernel_size"], 
                        stride=params["stride"], 
                        padding=params["padding"],
                        ceil_mode=params["ceil_mode"],
                        return_indices=params["return_indices"]);
    
    c, d, h, w = current_in_shape
    x = torch.randn(1, c, d, h, w);
    y = layer(x)
    current_in_shape = (y.shape[1], y.shape[2], y.shape[3], y.shape[4])

    return layer, current_in_shape



@accepts(dict, tuple, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_average_pooling1d(params, current_in_shape):

    in_channels = current_in_shape[0];

    layer = nn.AvgPool1d(params["kernel_size"], 
                        stride=params["stride"], 
                        padding=params["padding"]);
    
    c, w = current_in_shape
    x = torch.randn(1, c, w);
    y = layer(x)
    current_in_shape = (y.shape[1], y.shape[2])

    return layer, current_in_shape


@accepts(dict, tuple, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_average_pooling2d(params, current_in_shape):

    in_channels = current_in_shape[0];

    layer = nn.AvgPool2d(params["kernel_size"], 
                        stride=params["stride"], 
                        padding=params["padding"]);
    
    c, h, w = current_in_shape
    x = torch.randn(1, c, h, w);
    y = layer(x)
    current_in_shape = (y.shape[1], y.shape[2], y.shape[3])

    return layer, current_in_shape


@accepts(dict, tuple, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_average_pooling3d(params, current_in_shape):

    in_channels = current_in_shape[0];

    layer = nn.AvgPool3d(params["kernel_size"], 
                        stride=params["stride"], 
                        padding=params["padding"]);
    
    c, d, h, w = current_in_shape
    x = torch.randn(1, c, d, h, w);
    y = layer(x)
    current_in_shape = (y.shape[1], y.shape[2], y.shape[3], y.shape[4])

    return layer, current_in_shape


@accepts(dict, tuple, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_global_max_pooling1d(params, current_in_shape):

    in_channels = current_in_shape[0];

    layer = nn.AdaptiveMaxPool1d(output_size=1);
    
    c, w = current_in_shape
    x = torch.randn(1, c, w);
    y = layer(x)
    current_in_shape = (y.shape[1], y.shape[2])

    return layer, current_in_shape


@accepts(dict, tuple, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_global_max_pooling2d(params, current_in_shape):

    in_channels = current_in_shape[0];

    layer = nn.AdaptiveMaxPool2d(output_size=1);
    
    c, h, w = current_in_shape
    x = torch.randn(1, c, h, w);
    y = layer(x)
    current_in_shape = (y.shape[1], y.shape[2], y.shape[3])

    return layer, current_in_shape


@accepts(dict, tuple, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_global_max_pooling3d(params, current_in_shape):

    in_channels = current_in_shape[0];

    layer = nn.AdaptiveMaxPool3d(output_size=1);
    
    c, d, h, w = current_in_shape
    x = torch.randn(1, c, d, h, w);
    y = layer(x)
    current_in_shape = (y.shape[1], y.shape[2], y.shape[3], y.shape[4])

    return layer, current_in_shape


@accepts(dict, tuple, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_global_average_pooling1d(params, current_in_shape):

    in_channels = current_in_shape[0];

    layer = nn.AdaptiveAvgPool1d(output_size=1);
    
    c, w = current_in_shape
    x = torch.randn(1, c, w);
    y = layer(x)
    current_in_shape = (y.shape[1], y.shape[2])

    return layer, current_in_shape


@accepts(dict, tuple, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_global_average_pooling2d(params, current_in_shape):

    in_channels = current_in_shape[0];

    layer = nn.AdaptiveAvgPool2d(output_size=1);
    
    c, h, w = current_in_shape
    x = torch.randn(1, c, h, w);
    y = layer(x)
    current_in_shape = (y.shape[1], y.shape[2], y.shape[3])

    return layer, current_in_shape


@accepts(dict, tuple, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_global_average_pooling3d(params, current_in_shape):

    in_channels = current_in_shape[0];

    layer = nn.AdaptiveAvgPool3d(output_size=1);
    
    c, d, h, w = current_in_shape
    x = torch.randn(1, c, d, h, w);
    y = layer(x)
    current_in_shape = (y.shape[1], y.shape[2], y.shape[3], y.shape[4])

    return layer, current_in_shape



@accepts(dict, tuple, post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_flatten(params, current_in_shape):
        
    in_channels = current_in_shape[0];

    layer = nn.Flatten();

    if(len(current_in_shape) == 2):
        c, w = current_in_shape
        x = torch.randn(1, c, w);
        y = layer(x)
        current_in_shape = (y.shape[1])
    elif(len(current_in_shape) == 3):
        c, h, w = current_in_shape
        x = torch.randn(1, c, h, w);
        y = layer(x)
        current_in_shape = (y.shape[1])
    else:
        c, d, h, w = current_in_shape
        x = torch.randn(1, c, d, h, w);
        y = layer(x)
        current_in_shape = (y.shape[1])

    return layer, current_in_shape;


@accepts(dict, [int, tuple], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_fully_connected(params, current_in_shape):

    if(type(current_in_shape) == int):
        in_feat = current_in_shape;
    elif(type(current_in_shape) == tuple):
        in_feat = current_in_shape[0];

    layer = nn.Linear(in_feat, 
                    params["units"],
                    bias=params["use_bias"]);

    x = torch.randn(1, in_feat);
    y = layer(x)
    current_in_shape = (y.shape[1])

    return layer, current_in_shape;


@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_dropout(params, current_in_shape):
    
    layer = nn.Dropout(p=params["drop_probability"]);
    
    return layer, current_in_shape;


@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_identity(params, current_in_shape):
    
    layer = nn.Identity();
    
    return layer, current_in_shape;


@accepts(dict, [tuple, int],  post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_batch_normalization(params, current_in_shape):
    in_channels = current_in_shape[0];

    if(len(current_in_shape) == 2):
        layer = nn.BatchNorm1d(in_channels, 
                        eps=params["epsilon"], 
                        momentum=params["moving_average_momentum"], 
                        affine=params["use_trainable_parameters"], 
                        track_running_stats=params["use_trainable_parameters"])

    elif(len(current_in_shape) == 3):
        layer = nn.BatchNorm2d(in_channels, 
                        eps=params["epsilon"], 
                        momentum=params["moving_average_momentum"], 
                        affine=params["use_trainable_parameters"], 
                        track_running_stats=params["use_trainable_parameters"])

    elif(len(current_in_shape) == 4):
        layer = nn.BatchNorm3d(in_channels, 
                        eps=params["epsilon"], 
                        momentum=params["moving_average_momentum"], 
                        affine=params["use_trainable_parameters"], 
                        track_running_stats=params["use_trainable_parameters"])


    return layer, current_in_shape;



@accepts(dict, [tuple, int],  post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_instance_normalization(params, current_in_shape):
    in_channels = current_in_shape[0];

    if(len(current_in_shape) == 2):
        layer = nn.InstanceNorm1d(in_channels, 
                        eps=params["epsilon"], 
                        momentum=params["moving_average_momentum"], 
                        affine=params["use_trainable_parameters"], 
                        track_running_stats=params["use_trainable_parameters"])

    elif(len(current_in_shape) == 3):
        layer = nn.InstanceNorm2d(in_channels, 
                        eps=params["epsilon"], 
                        momentum=params["moving_average_momentum"], 
                        affine=params["use_trainable_parameters"], 
                        track_running_stats=params["use_trainable_parameters"])

    elif(len(current_in_shape) == 4):
        layer = nn.InstanceNorm3d(in_channels, 
                        eps=params["epsilon"], 
                        momentum=params["moving_average_momentum"], 
                        affine=params["use_trainable_parameters"], 
                        track_running_stats=params["use_trainable_parameters"])


    return layer, current_in_shape;



@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_layer_layer_normalization(params, current_in_shape):
    layer = nn.LayerNorm(list(current_in_shape), 
                        eps=params["epsilon"], 
                        elementwise_affine=params["use_trainable_parameters"]);
    return layer, current_in_shape;



@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_relu(params, current_in_shape):
    layer = nn.ReLU();
    return layer, current_in_shape;


@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_sigmoid(params, current_in_shape):
    layer = nn.Sigmoid();
    return layer, current_in_shape;


@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_tanh(params, current_in_shape):
    layer = nn.Tanh();
    return layer, current_in_shape;

@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_softplus(params, current_in_shape):
    layer = nn.Softplus(beta=params["beta"], 
                            threshold=params["threshold"]);
    return layer, current_in_shape;


@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_softsign(params, current_in_shape):
    layer = nn.Softsign();
    return layer, current_in_shape;



@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_elu(params, current_in_shape):
    layer = nn.ELU(alpha=params["alpha"]);
    return layer, current_in_shape;


@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_leaky_relu(params, current_in_shape):
    layer = nn.LeakyReLU(negative_slope=params["alpha"]);
    return layer, current_in_shape;


@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_prelu(params, current_in_shape):
    layer = nn.PReLU();
    return layer, current_in_shape;


@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_selu(params, current_in_shape):
    layer = nn.SELU();
    return layer, current_in_shape;


@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_hardshrink(params, current_in_shape):
    layer = nn.Hardshrink(lambd=params["threshold"]);
    return layer, current_in_shape;


@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_hardtanh(params, current_in_shape):
    layer = nn.Hardtanh(min_val=params["min_val"],
                            max_val=params["max_val"]);
    return layer, current_in_shape;


@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_logsigmoid(params, current_in_shape):
    layer = nn.LogSigmoid();
    return layer, current_in_shape;


@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_relu6(params, current_in_shape):
    layer = nn.ReLU6();
    return layer, current_in_shape;


@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_rrelu(params, current_in_shape):
    layer = nn.RReLU();
    return layer, current_in_shape;


@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_celu(params, current_in_shape):
    layer = nn.CELU(alpha=params["alpha"]);
    return layer, current_in_shape;


@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_softshrink(params, current_in_shape):
    layer = nn.Softshrink(lambd=params["threshold"]);
    return layer, current_in_shape;



@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_tanhshrink(params, current_in_shape):
    layer = nn.Tanhshrink();
    return layer, current_in_shape;


@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_threshold(params, current_in_shape):
    layer = nn.Threshold(params["threshold"], 
                            params["value"]);
    return layer, current_in_shape;


@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_softmin(params, current_in_shape):
    layer = nn.Softmin();
    return layer, current_in_shape;


@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_softmax(params, current_in_shape):
    layer = nn.Softmax();
    return layer, current_in_shape;


@accepts(dict, [tuple, int], post_trace=True)
@TraceFunction(trace_args=True, trace_rv=False)
def custom_model_activation_logsoftmax(params, current_in_shape):
    layer = nn.LogSoftmax();
    return layer, current_in_shape;


class Net_Add(nn.Module):

    def __init__(self, branches):
        super().__init__()
        self.child_names = [];
        
        for i in range(len(branches)):
            vars(self)["body" + str(i)] = nn.Sequential();
            for j in range(len(branches[i])):
                vars(self)["body" + str(i)].add_module("br_{}_{}".format(i, j), branches[i][j]);
            self.child_names.append("body" + str(i));
                
              
        for i, child in enumerate(self.child_names):
            setattr(self, 'body{0}'.format(i), vars(self)["body" + str(i)])
        
        
        
    def forward(self, x):
        for i in range(len(self.child_names)):
            br = getattr(self, 'body{0}'.format(i));
            if(i==0):
                y = br(x);
            else:
                y = y + br(x);
        return y



class Net_Concat(nn.Module):

    def __init__(self, branches):
        super().__init__()
        self.child_names = [];
        
        for i in range(len(branches)):
            vars(self)["body" + str(i)] = nn.Sequential();
            for j in range(len(branches[i])):
                vars(self)["body" + str(i)].add_module("br_{}_{}".format(i, j), branches[i][j]);
            self.child_names.append("body" + str(i));
                
              
        for i, child in enumerate(self.child_names):
            setattr(self, 'body{0}'.format(i), vars(self)["body" + str(i)])
        
        
        
    def forward(self, x):
        outs = [];
        for i in range(len(self.child_names)):
            br = getattr(self, 'body{0}'.format(i));
            outs.append(br(x));
        return torch.cat(tuple(outs), 1)