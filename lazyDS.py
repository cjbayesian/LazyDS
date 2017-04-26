import os
import cPickle


def get_user_vars():
    """
    Get variables in user namespace (ripped directly from ipython namespace
    magic code)
    """
    import IPython
    ip = IPython.get_ipython()
    user_ns = ip.user_ns
    user_ns_hidden = ip.user_ns_hidden
    nonmatching = object()
    var_hist = [i for i in user_ns
                if not i.startswith('_')
                and (user_ns[i] is not user_ns_hidden.get(i, nonmatching))]

    var_dict = {k: user_ns[k] for k in var_hist}
    return var_dict


def get_vars_to_save():
    do_not_save_types = ["<type 'function'>",
                         "<type 'module'>",
                         "<type 'type'>",
                         "<class 'pymongo.mongo_client.MongoClient'>"]

    save_vars = {k: v for k, v in get_user_vars().items()
                 if str(type(v)) not in do_not_save_types}

    return save_vars


def save_obj(obj, var_name, path):
    with open(os.path.join(path, var_name), 'wb') as f:
        cPickle.dump(obj, f, cPickle.HIGHEST_PROTOCOL)


def load_obj(var_name, path):
    with open(os.path.join(path, var_name), 'rb') as f:
        var = cPickle.load(f)
    return var


def save_session(path='tmp_session'):
    if not os.path.exists(path):
        os.makedirs(path)
    vars_to_save = get_vars_to_save()
    for k,v in vars_to_save.items():
        print "saving", k
        try:
            save_obj(v, k, path)
        except:
            print "ERROR - Could not save", k


def load_session(path='tmp_session'):
    if not os.path.exists(path):
        print path, 'does not exist'
        return None

    var_list = os.listdir(path)
    var_dict = {}
    for var_name in var_list:
        print 'loading', var_name
        var_dict[var_name] = load_obj(var_name, path)

    return var_dict
