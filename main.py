import time

from velodyne import *

def main():
    config_path = './config/Alpha Prime.xml'
    data_path = './data/skip_toh_demo.pcap'
    output_path = './runs/test'

    vd = VelodyneDecoder(config_path=config_path, pcap_path=data_path, output_path=output_path)

    t_last = time.time()
    while 1:
        vd.decode_next_packet()
        if vd.judge_jump_cut_degree():
            vd.generate_frame(pcd_file_type='pcd')
            t = time.time()
            print('    {:.2f} s'.format(t - t_last))
            t_last = time.time()


if __name__ == '__main__':
    main()
