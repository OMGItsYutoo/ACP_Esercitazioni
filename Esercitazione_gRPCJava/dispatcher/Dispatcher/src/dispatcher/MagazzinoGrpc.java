package dispatcher;

import static io.grpc.MethodDescriptor.generateFullMethodName;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.73.0)",
    comments = "Source: magazzino.proto")
@io.grpc.stub.annotations.GrpcGenerated
public final class MagazzinoGrpc {

  private MagazzinoGrpc() {}

  public static final java.lang.String SERVICE_NAME = "dispatcher.Magazzino";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<dispatcher.Item,
      dispatcher.Empty> getDepositaMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "deposita",
      requestType = dispatcher.Item.class,
      responseType = dispatcher.Empty.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<dispatcher.Item,
      dispatcher.Empty> getDepositaMethod() {
    io.grpc.MethodDescriptor<dispatcher.Item, dispatcher.Empty> getDepositaMethod;
    if ((getDepositaMethod = MagazzinoGrpc.getDepositaMethod) == null) {
      synchronized (MagazzinoGrpc.class) {
        if ((getDepositaMethod = MagazzinoGrpc.getDepositaMethod) == null) {
          MagazzinoGrpc.getDepositaMethod = getDepositaMethod =
              io.grpc.MethodDescriptor.<dispatcher.Item, dispatcher.Empty>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "deposita"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  dispatcher.Item.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  dispatcher.Empty.getDefaultInstance()))
              .setSchemaDescriptor(new MagazzinoMethodDescriptorSupplier("deposita"))
              .build();
        }
      }
    }
    return getDepositaMethod;
  }

  private static volatile io.grpc.MethodDescriptor<dispatcher.Empty,
      dispatcher.Item> getPrelevaMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "preleva",
      requestType = dispatcher.Empty.class,
      responseType = dispatcher.Item.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<dispatcher.Empty,
      dispatcher.Item> getPrelevaMethod() {
    io.grpc.MethodDescriptor<dispatcher.Empty, dispatcher.Item> getPrelevaMethod;
    if ((getPrelevaMethod = MagazzinoGrpc.getPrelevaMethod) == null) {
      synchronized (MagazzinoGrpc.class) {
        if ((getPrelevaMethod = MagazzinoGrpc.getPrelevaMethod) == null) {
          MagazzinoGrpc.getPrelevaMethod = getPrelevaMethod =
              io.grpc.MethodDescriptor.<dispatcher.Empty, dispatcher.Item>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "preleva"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  dispatcher.Empty.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  dispatcher.Item.getDefaultInstance()))
              .setSchemaDescriptor(new MagazzinoMethodDescriptorSupplier("preleva"))
              .build();
        }
      }
    }
    return getPrelevaMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static MagazzinoStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<MagazzinoStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<MagazzinoStub>() {
        @java.lang.Override
        public MagazzinoStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new MagazzinoStub(channel, callOptions);
        }
      };
    return MagazzinoStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports all types of calls on the service
   */
  public static MagazzinoBlockingV2Stub newBlockingV2Stub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<MagazzinoBlockingV2Stub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<MagazzinoBlockingV2Stub>() {
        @java.lang.Override
        public MagazzinoBlockingV2Stub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new MagazzinoBlockingV2Stub(channel, callOptions);
        }
      };
    return MagazzinoBlockingV2Stub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static MagazzinoBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<MagazzinoBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<MagazzinoBlockingStub>() {
        @java.lang.Override
        public MagazzinoBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new MagazzinoBlockingStub(channel, callOptions);
        }
      };
    return MagazzinoBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static MagazzinoFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<MagazzinoFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<MagazzinoFutureStub>() {
        @java.lang.Override
        public MagazzinoFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new MagazzinoFutureStub(channel, callOptions);
        }
      };
    return MagazzinoFutureStub.newStub(factory, channel);
  }

  /**
   */
  public interface AsyncService {

    /**
     */
    default void deposita(dispatcher.Item request,
        io.grpc.stub.StreamObserver<dispatcher.Empty> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getDepositaMethod(), responseObserver);
    }

    /**
     */
    default void preleva(dispatcher.Empty request,
        io.grpc.stub.StreamObserver<dispatcher.Item> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getPrelevaMethod(), responseObserver);
    }
  }

  /**
   * Base class for the server implementation of the service Magazzino.
   */
  public static abstract class MagazzinoImplBase
      implements io.grpc.BindableService, AsyncService {

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return MagazzinoGrpc.bindService(this);
    }
  }

  /**
   * A stub to allow clients to do asynchronous rpc calls to service Magazzino.
   */
  public static final class MagazzinoStub
      extends io.grpc.stub.AbstractAsyncStub<MagazzinoStub> {
    private MagazzinoStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected MagazzinoStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new MagazzinoStub(channel, callOptions);
    }

    /**
     */
    public void deposita(dispatcher.Item request,
        io.grpc.stub.StreamObserver<dispatcher.Empty> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getDepositaMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void preleva(dispatcher.Empty request,
        io.grpc.stub.StreamObserver<dispatcher.Item> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getPrelevaMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   * A stub to allow clients to do synchronous rpc calls to service Magazzino.
   */
  public static final class MagazzinoBlockingV2Stub
      extends io.grpc.stub.AbstractBlockingStub<MagazzinoBlockingV2Stub> {
    private MagazzinoBlockingV2Stub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected MagazzinoBlockingV2Stub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new MagazzinoBlockingV2Stub(channel, callOptions);
    }

    /**
     */
    public dispatcher.Empty deposita(dispatcher.Item request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getDepositaMethod(), getCallOptions(), request);
    }

    /**
     */
    public dispatcher.Item preleva(dispatcher.Empty request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getPrelevaMethod(), getCallOptions(), request);
    }
  }

  /**
   * A stub to allow clients to do limited synchronous rpc calls to service Magazzino.
   */
  public static final class MagazzinoBlockingStub
      extends io.grpc.stub.AbstractBlockingStub<MagazzinoBlockingStub> {
    private MagazzinoBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected MagazzinoBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new MagazzinoBlockingStub(channel, callOptions);
    }

    /**
     */
    public dispatcher.Empty deposita(dispatcher.Item request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getDepositaMethod(), getCallOptions(), request);
    }

    /**
     */
    public dispatcher.Item preleva(dispatcher.Empty request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getPrelevaMethod(), getCallOptions(), request);
    }
  }

  /**
   * A stub to allow clients to do ListenableFuture-style rpc calls to service Magazzino.
   */
  public static final class MagazzinoFutureStub
      extends io.grpc.stub.AbstractFutureStub<MagazzinoFutureStub> {
    private MagazzinoFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected MagazzinoFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new MagazzinoFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<dispatcher.Empty> deposita(
        dispatcher.Item request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getDepositaMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<dispatcher.Item> preleva(
        dispatcher.Empty request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getPrelevaMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_DEPOSITA = 0;
  private static final int METHODID_PRELEVA = 1;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final AsyncService serviceImpl;
    private final int methodId;

    MethodHandlers(AsyncService serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_DEPOSITA:
          serviceImpl.deposita((dispatcher.Item) request,
              (io.grpc.stub.StreamObserver<dispatcher.Empty>) responseObserver);
          break;
        case METHODID_PRELEVA:
          serviceImpl.preleva((dispatcher.Empty) request,
              (io.grpc.stub.StreamObserver<dispatcher.Item>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  public static final io.grpc.ServerServiceDefinition bindService(AsyncService service) {
    return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
        .addMethod(
          getDepositaMethod(),
          io.grpc.stub.ServerCalls.asyncUnaryCall(
            new MethodHandlers<
              dispatcher.Item,
              dispatcher.Empty>(
                service, METHODID_DEPOSITA)))
        .addMethod(
          getPrelevaMethod(),
          io.grpc.stub.ServerCalls.asyncUnaryCall(
            new MethodHandlers<
              dispatcher.Empty,
              dispatcher.Item>(
                service, METHODID_PRELEVA)))
        .build();
  }

  private static abstract class MagazzinoBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    MagazzinoBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return dispatcher.MagazzinoOuterClass.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("Magazzino");
    }
  }

  private static final class MagazzinoFileDescriptorSupplier
      extends MagazzinoBaseDescriptorSupplier {
    MagazzinoFileDescriptorSupplier() {}
  }

  private static final class MagazzinoMethodDescriptorSupplier
      extends MagazzinoBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final java.lang.String methodName;

    MagazzinoMethodDescriptorSupplier(java.lang.String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (MagazzinoGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new MagazzinoFileDescriptorSupplier())
              .addMethod(getDepositaMethod())
              .addMethod(getPrelevaMethod())
              .build();
        }
      }
    }
    return result;
  }
}
