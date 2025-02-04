#!/usr/bin/env python3

# Train A2C on slimevolley.

import os
import gym
import slimevolleygym
import maze
from slimevolleygym import SurvivalRewardEnv

from stable_baselines.common.policies import MlpPolicy
from stable_baselines import logger
from stable_baselines.common.callbacks import EvalCallback
from stable_baselines import A2C
from stable_baselines.common import make_vec_env


NUM_TIMESTEPS = int(1e7)
EVAL_FREQ = 250000
EVAL_EPISODES = 1000

def slimeVolley():
    LOGDIR = "a2c" # moved to zoo afterwards.

    logger.configure(folder=LOGDIR)
    
    env = make_vec_env('SlimeVolley-v0', n_envs=1) # vectorized environment

    model = A2C(MlpPolicy, env, tensorboard_log=LOGDIR, verbose=0, lr_schedule='linear', ent_coef=0.001, 
        gamma=0.995, vf_coef=0.4, learning_rate=0.0008)

    eval_callback = EvalCallback(env, best_model_save_path=LOGDIR, log_path=LOGDIR, eval_freq=EVAL_FREQ, n_eval_episodes=EVAL_EPISODES)

    model.learn(total_timesteps=NUM_TIMESTEPS, callback=eval_callback)

    model.save(os.path.join(LOGDIR, "final_model")) # probably never get to this point.

    env.close()


def mazeWorld():

    LOGDIR = "a2c_maze" # moved to zoo afterwards.

    logger.configure(folder=LOGDIR)

    env = make_vec_env('Maze-Easy-v0', n_envs=1)

    model = A2C(MlpPolicy, env, tensorboard_log=LOGDIR, verbose=0)

    eval_callback = EvalCallback(env, best_model_save_path=LOGDIR, log_path=LOGDIR, eval_freq=EVAL_FREQ, n_eval_episodes=EVAL_EPISODES)

    model.learn(total_timesteps=NUM_TIMESTEPS, callback=eval_callback)

    model.save(os.path.join(LOGDIR, "final_model")) # probably never get to this point.

    env.close()


if __name__=="__main__":
    slimeVolley()
    mazeWorld()






