from easydict import EasyDict

bigfish_ppg_default_config = dict(
    exp_name='bigfish_ppg_seed0',
    env=dict(
        is_train=True,
        env_id='bigfish',
        collector_env_num=64,
        evaluator_env_num=10,
        n_evaluator_episode=50,
        stop_value=40,
        manager=dict(
            shared_memory=True,
        ),
    ),
    policy=dict(
        cuda=True,
        model=dict(
            obs_shape=[3, 64, 64],
            action_shape=15,
            encoder_hidden_size_list=[16,32,32],
            actor_head_hidden_size=256,
            critic_head_hidden_size=256,
            impala_cnn_encoder=True,
        ),
        learn=dict(
            learning_rate=0.0005,
            actor_epoch_per_collect=1,
            critic_epoch_per_collect=1,
            value_norm=True,
            batch_size=16384,
            value_weight=0.5,
            entropy_weight=0.01,
            clip_ratio=0.2,
            aux_freq=1,
        ),
        collect=dict(n_sample=16384, ),
        eval=dict(evaluator=dict(eval_freq=96, )),
        other=dict(
        ),
    ),
)
bigfish_ppg_default_config = EasyDict(bigfish_ppg_default_config)
main_config = bigfish_ppg_default_config

bigfish_ppg_create_config = dict(
    env=dict(
        type='procgen',
        import_names=['dizoo.procgen.envs.procgen_env'],
    ),
    env_manager=dict(type='subprocess', ),
    policy=dict(type='ppg'),
)
bigfish_ppg_create_config = EasyDict(bigfish_ppg_create_config)
create_config = bigfish_ppg_create_config

if __name__ == "__main__":

    from ding.entry import serial_pipeline_onpolicy_ppg
    serial_pipeline_onpolicy_ppg([main_config, create_config], seed=0)
