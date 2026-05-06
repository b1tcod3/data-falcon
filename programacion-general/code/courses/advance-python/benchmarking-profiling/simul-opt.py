            from matplotlib import pyplot as plt
        from matplotlib import animation
        from random import uniform

class Particle:
    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel

class ParticleSimulator:
    def __init__(self, particles):
        self.particles = particles


    def evolve(self, dt):
        timestep = 0.00001
        nsteps = int(dt / timestep)

        for i in range(nsteps):
            for p in self.particles:
                # 1. calculate the direction of the velocity
                t_x_ang = timestep * p.ang_vel
                for i in range(nsteps):
                    norm = (p.x**2 + p.y**2)**0.5
                    p.x , p.y = (p.x - t_x_ang * p.y/norm,
                                 p.y + t_x_ang * p.x/norm)

def visualize(simulator):

    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig  = plt.figure()
    ax = plt.subplot(111, aspect='equal')
    line, = ax.plot(X, Y, 'ro')

    # Axis limits
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    # It will be run when the animation starts
    def init():
        line.set_data(X, Y)
        return line,

    def animate(i):
        # We let the particles evolve for 0.01 time units
        simulator.evolve(0.01)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]
        line.set_data(X, Y)
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func=init, blit=True,interval=10)
    plt.show()

def test_visualize():
    particles = [
        Particle(0.3, 0.5, 1),
        Particle(0.0,-0.5, 2),
        Particle(-0.1,-0.4, 3),
    ]
    simulator = ParticleSimulator(particles)
    visualize(simulator)

def test_evolve():
    particles = [ Particle( 0.3, 0.5, +1),
                  Particle( 0.0, -0.5, -1),
                  Particle(-0.1, -0.4, +3)
                 ]

    p0, p1, p2, = particles

    simulator = ParticleSimulator(particles)

    simulator.evolve(0.1)
    def fequal(a,b, eps=1e-5):
        return abs(a-b) < eps

    assert fequal(p0.x, 0.210269)
    assert fequal(p0.y, 0.543863)

    assert fequal(p0.x, 0.210269)
    assert fequal(p0.y, 0.543863)

def benchmark():
    particles = [
        Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0),
                 uniform(-1.0, 1.0))
        for i in range(1000)
    ]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)

    
# if __name__ == "__main__":
   # test_visualize()
   # test_evolve()
   # benchmark()
